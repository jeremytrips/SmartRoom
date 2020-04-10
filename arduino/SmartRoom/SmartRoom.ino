#include <EEPROM.h>
#include "WiFi.h"

// Pinout declaration for the info RGB pin. Color will be described in the table doc.
#define infoPinR 19
#define infoPinG 18
#define infoPinB 5
#define WRITEN_CONSTANT 0x55

#define debug false

struct pin {
  int pin: null;
  int value;
}

struct data {
  pin red;
  pin green;
  pin blue;
}

// Variable declaration.

char temp[50];
char host[50] = {0};
int port = -1;
int id = -1;
char ssid[50] = {0};
char password[50] = {0};

WiFiClient client;

// Function prototype.
void EEPROM_write(char arrayToWrite[], int firstIndex);
void EEPROM_read(char* arrayToRead, int firstIndex);
void resetArray(char* arrayToReset[]);
void setupWifiData();
int arrayToInt(char array[]);
void setDigitalValue(int pin, int value);

void setup() {
  Serial.begin(115200);

  pinMode(2, OUTPUT);

  pinMode(infoPinR, OUTPUT);
  pinMode(infoPinG, OUTPUT);
  pinMode(infoPinB, OUTPUT);

  // Pin needs to be high for the led to be off as it is anode one.
  digitalWrite(infoPinR, HIGH);
  digitalWrite(infoPinG, HIGH);
  digitalWrite(infoPinB, HIGH);

  delay(5000);

  if (Serial.available()) {
    for (int i = 0; i < 10; i++)
      Serial.write('B');
    setupWifiData();
  }

  EEPROM.begin(512);
  if (EEPROM.read(511) != WRITEN_CONSTANT) {
    // Start Serial comunication for setup.
    Serial.println("serial");
    setupWifiData();
  }
  else {
    /* Start the wifi protocol comunication.
       The blue led will blink until the connection occurs.
       After 10 try, the esp switch on a red led to warn the user.
    */
    Serial.println("Wifi");
    // Read server data in EEPROM.
    int connection_try = 0;
    EEPROM_read(host, 300);
    EEPROM_read(temp, 350);
    EEPROM_read(ssid, 400);
    EEPROM_read(password, 450);
    port = arrayToInt(temp);

    Serial.print("SSID: ");
    Serial.println(ssid);
    Serial.print("Password: ");
    Serial.println(password);
    Serial.print("Host: ");
    Serial.println(host);
    Serial.print("Port: ");
    Serial.println(port);

    WiFi.begin(ssid, password);
    while (WiFi.status() != WL_CONNECTED) {
      // Checking the wifi status every 500 ms.
      delay(500);
      connection_try++;
      Serial.print("Connection attempt: ");
      Serial.println(connection_try);
      if (connection_try > 10) {
        // Error as occurs the SSID or password may be wrong.
        digitalWrite(infoPinR, !digitalRead(infoPinR));
      } else {
        digitalWrite(infoPinB, !digitalRead(infoPinB));
      }
    }
    digitalWrite(infoPinB, HIGH);
    Serial.println("Connected");
  }

  EEPROM.end();

  unsigned long previousMillis = 0;
  const int delay = 1000;

  if (!client.connect(host, port)) {
    // if the module can't connect to the server. Provided data may be wrong and so red led is turned on.
    digitalWrite(infoPinR, LOW);
    while (true);
  } else {
    // Introduction to the server

    if (EEPROM.read(510) == WRITEN_CONSTANT) {
      client.write("no_name");
      resetArray(temp);
      while (!client.available());
      client.readStringUntil('%').toCharArray(temp, 50);

      Serial.print("Recieced_name: ");
      Serial.println(temp);

      EEPROM_write(temp, 0);
      EEPROM.write(510, WRITEN_CONSTANT);
      EEPROM.commit();
    } else {
      resetArray(temp);
      EEPROM_read(temp, 0);
      client.print(temp);
    }
  }
}

unsigned long previousMillis = 0;
const int timeDelay = 1000;

void loop() {
  /*
     TODO
  */
  // Connection to the server.


  unsigned long currentMillis = millis();
  if (currentMillis - previousMillis >= timeDelay) {
    previousMillis = currentMillis;
    digitalWrite(infoPinG, !digitalRead(infoPinG));
  }

  if (client.available()) {
    // Data has been sended by the server. The data frame is described in the doc.
    String tmp = client.readStringUntil('%');
  }
}


int arrayToInt(char array[]) {
  /*
     Take an array of char as parameter that has been readed in the EEPROM.
     The array contains only different int.
     The function loop through the array and multiply the int by the corresponding factor.
     The port number is an unsigned 16-bit integer, so maximum 65535. the max factor is then 10000
  */
  double toReturn = 0;
  for (int i = 0; i < 4 ; i++) {
    int tmp = array[i] - '0';
    double factor = pow(10, (3 - i));
    toReturn += tmp * factor;
  }
  return toReturn;
}

void setupWifiData() {
  /*
     Usualy the first boot of the esp32. This loop is used to save data in the esp32 EEPROM.
     The esp32 memory map is in the data.
     The App software is need to check the length of the sended data. It must be lower than 50 chars.
     In that configuration the info led will blink in green every second.
  */

  Serial.begin(115200);
  Serial.setTimeout(2000);
  Serial.println("Setting up things");
  int writen = 0;
  char tmp[50];
  char action;
  bool run = true;
  unsigned long previousMillis = 0;
  const int delay = 1000;
  while (run) {
    /*
       µc will receive data from the app through UART.
       Those will be stored in the EEPROM folowing the memory table that has been draw.
       The 48 char represent the action to do.
    */

    unsigned long currentMillis = millis();

    if (currentMillis - previousMillis >= delay) {
      previousMillis = currentMillis;
      digitalWrite(infoPinG, !digitalRead(infoPinG));
      Serial.println(writen);
    }

    if (Serial.available()) {
      String str = Serial.readStringUntil('%');
      str.toCharArray(tmp, 50);
      action = tmp[48];
      Serial.println(tmp);
      Serial.println(action);
      while (Serial.available())
        Serial.read();
    }
    switch (action) {
      case 's':
        // Writing the Ssid
        EEPROM_write(tmp, 400);
        writen++;
        break;
      case 'p':
        // Writing the Password
        EEPROM_write(tmp, 450);
        writen++;
        break;
      case 'i':
        // Writing server Ip
        EEPROM_write(tmp, 300);
        writen++;
        break;
      case 'o':
        // Writing server pOrt
        EEPROM_write(tmp, 350);
        writen++;
        break;
      case 'n':
        // Nothing to do
        break;
      default:
        // Error action doesn't match. Warn user.
        break;
    }
    action = 'n';
    if (writen == 4) {
      run = false;
      EEPROM.write(511, WRITEN_CONSTANT);
    }
  }
  digitalWrite(infoPinG, HIGH);
  EEPROM.commit();
  ESP.restart();
}

void resetArray(char* arrayToReset) {
  // Take a pointer array as argument and reset it to Null char (0).
  for (int i = 0; i < 50; ++i)
    arrayToReset[i] = 0;
}

void EEPROM_read(char* arrayToRead, int firstIndex) {
  // Read the EEPROM from firstIndex and write readed data into the arrayToRead
  for (int i = 0; i < 50; i++) {
    if (EEPROM.read(firstIndex + i) != ' ') {
      arrayToRead[i] = EEPROM.read(firstIndex + i);
    } else {
      break;
    }
  }
}

void EEPROM_write(char arrayToWrite[], int firstIndex) {
  // Write the arrayToWrite array in the EEPROM starting at the firstIndex index.

  for (int i = 0; i < 50; i++) {
    if (arrayToWrite[i] != ' ') {
      EEPROM.write(firstIndex + i, arrayToWrite[i]);
    } else {
      EEPROM.write(firstIndex + i, 0);
    }
  }
  EEPROM.commit();
}
