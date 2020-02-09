#include <EEPROM.h>
#include "WiFi.h"

// Constal
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
  EEPROM.begin(512);
  if(EEPROM.read(511) != 0x55){
    // Start Serial comunication for setup.
    setupWifiData();
  } else {
    // Start the wifi protocol comunication.
        
    EEPROM_read(ssid, 401);
    EEPROM_read(password, 451);
    
    WiFi.begin(ssid, password);
    while (WiFi.status() != WL_CONNECTED) {
      delay(500);
      digitalWrite(2, not digitalRead(2));
    }
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
   */
  bool run = true;
  Serial.begin(115200);
  Serial.setTimeout(2000);
  int writen = 0;
  char tmp[50];
  char action;
  Serial.println("Serial");  
  while(run){
    // µc will receive data from the app through UART. Those will be stored in the EEPROM folowing the memory table that has been draw.
    if(Serial.available()){
      String str = Serial.readStringUntil('%');
      str.toCharArray(tmp, 50);
      Serial.println(tmp);
      action = tmp[48];
      Serial.println(action);
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
    if(writen == 2){
      run = false;
      EEPROM.write(511, 0x55);
    }
  }
  EEPROM.commit();
  ESP.restart();
}

void resetArray(char* arrayToReset){
  // Take a pointer array as argument and reset it to ' '.
  for (int i = 0; i < 50; ++i)
    arrayToReset[i] = ' ';
}

void EEPROM_read(char* arrayToRead, int firstIndex){
  for(int i = 0; i<50; i++){
    if(EEPROM.read(firstIndex+i) != ' '){
      arrayToRead[i] = EEPROM.read(firstIndex+i);
    } else {
      break;
    }
  }
}

void EEPROM_write(char arrayToWrite[], int firstIndex){
  for(int i= 0; i<50; i++){
    if(arrayToWrite[i] != ' '){
      EEPROM.write(firstIndex+i, arrayToWrite[i]);
    } else {
      EEPROM.write(firstIndex+i, 0);
    }
  }
  EEPROM.commit();
}
