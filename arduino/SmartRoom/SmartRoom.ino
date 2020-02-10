#include <EEPROM.h>
#include "WiFi.h"

// Pinout declaration for the info RGB pin. Color will be described in the table doc.
#define infoPinR 13  
#define infoPinG 14
#define infoPinB 15

// Variable declaration.
char ssid[50];
char password[50];

// Function prototype.
void EEPROM_write(char arrayToWrite[], int firstIndex);
void EEPROM_read(char* arrayToRead, int firstIndex);
void resetArray(char* arrayToReset[]);
void setupWifiData();

void setup() {
  // put your setup code here, to run once:
  pinMode(2, OUTPUT);

  pinMode(infoPinR, OUTPUT);
  pinMode(infoPinG, OUTPUT);
  pinMode(infoPinB, OUTPUT);

  // Pin needs to be high for the led to be off as it is anode one.
  digitalWrite(infoPinR, HIGH);
  digitalWrite(infoPinG, HIGH);
  digitalWrite(infoPinB, HIGH);

  EEPROM.begin(512);
  if(EEPROM.read(511) != 0x55){
    // Start Serial comunication for setup.
    setupWifiData();
  } else {
    /* Start the wifi protocol comunication.
     * The blue led will blink until the connection occurs. 
     * After 10 try, the esp switch on a red led to warn the user. 
     */
    int connection_try = 0;
    EEPROM_read(ssid, 401);
    EEPROM_read(password, 451);
    
    WiFi.begin(ssid, password);
    while (WiFi.status() != WL_CONNECTED) {
      // Checking the wifi status every 500 ms.
      delay(500);
      connection_try++;
      if(connection_try>10){
        // Error as occurs the SSID or password may be wrong. 
        digitalWrite(infoPinR, !digitalRead(infoPinR));
      } else {
        digitalWrite(infoPinB, !digitalRead(infoPinB));
      }
    }
    digitalWrite(infoPinB, HIGH);
  }

  EEPROM.end();

}

void loop() {
  // put your main code here, to run repeatedly:
}

void setupWifiData(){
  /*
   * Normaly the first boot of the esp32. This loop is used to save data in the esp32 EEPROM.
   * The esp32 memory map is in the data. 
   * The App software is need to check the length of the sended data. It must be lower than 50 chars.
   * In that configuration the info led will blink in green every second. 
   */
  
  Serial.begin(115200);
  Serial.setTimeout(2000);

  int writen = 0;
  char tmp[50];
  char action;
  bool run = true;
  unsigned long previousMillis = 0;
  const int delay = 1000;

  while(run){
    /* µc will receive data from the app through UART. 
     * Those will be stored in the EEPROM folowing the memory table that has been draw.
     * The 48 char represent the action to do.
     */

    unsigned long currentMillis = millis();

    if (currentMillis - previousMillis >= delay) {
      // save the last time you blinked the LED
      previousMillis = currentMillis;
      digitalWrite(infoPinG, !digitalRead(infoPinG));
    }

    if(Serial.available()){
      String str = Serial.readStringUntil('%');
      str.toCharArray(tmp, 50);
      action = tmp[48];
      Serial.read();
    }
    switch (action){
      case 's': 
        // Writing the SSID
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
    if(writen == 4){
      run = false;
      EEPROM.write(511, 0x55);
    }
  }
  digitalWrite(infoPinG, HIGH);
  EEPROM.commit();
  ESP.restart();
}

void resetArray(char* arrayToReset){
  // Take a pointer array as argument and reset it to Null char (0).
  for (int i = 0; i < 50; ++i)
    arrayToReset[i] = 0;
}

void EEPROM_read(char* arrayToRead, int firstIndex){
  // Read the EEPROM from firstIndex and write readed data into the arrayToRead
  for(int i = 0; i<50; i++){
    if(EEPROM.read(firstIndex+i) != ' '){
      arrayToRead[i] = EEPROM.read(firstIndex+i);
    } else {
      break;
    }
  }
}

void EEPROM_write(char arrayToWrite[], int firstIndex){
  // Write the arrayToWrite array in the EEPROM starting at the firstIndex index.

  for(int i= 0; i<50; i++){
    if(arrayToWrite[i] != ' '){
      EEPROM.write(firstIndex+i, arrayToWrite[i]);
    } else {
      EEPROM.write(firstIndex+i, 0);
    }
  }
  EEPROM.commit();
}
