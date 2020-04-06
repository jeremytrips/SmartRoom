#include <EEPROM.h>
#include "WiFi.h"

// Pinout declaration for the info RGB pin. Color will be described in the table doc.
#define infoPinR 19
#define infoPinG 18
#define infoPinB 5

#define debug false

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
  
  EEPROM.begin(512);
  EEPROM_read(host, 301);
  EEPROM_read(temp, 351);
  EEPROM_read(ssid, 401);
  EEPROM_read(password, 451);
  port = arrayToInt(temp);
  EEPROM.end();

  Serial.print("SSID: ");
  Serial.println(ssid);
  Serial.print("Password: ");
  Serial.println(password);
  Serial.print("Host: ");
  Serial.println(host);
  Serial.print("Port: ");
  Serial.println(port);
}

void loop() {
  /*
     TODO
  */
  // Connection to the server.


  setupWifiData();

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
    }

    if (Serial.available()) {
      String str = Serial.readStringUntil('%');
      str.toCharArray(tmp, 50);
      action = tmp[48];
      Serial.read();
    }
    switch (action) {
      case 's':
        // Writing the Ssid
        EEPROM_write(tmp, 401);
        writen++;
        break;
      case 'p':
        // Writing the Password
        EEPROM_write(tmp, 451);
        writen++;
        break;
      case 'i':
        // Writing server Ip
        EEPROM_write(tmp, 301);
        writen++;
        break;
      case 'o':
        // Writing server pOrt
        EEPROM_write(tmp, 351);
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
      EEPROM.write(511, 0x55);
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
