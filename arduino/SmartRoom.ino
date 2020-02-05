#include <EEPROM.h>


void EEPROM_writeSring(int startIndex, String data);
void setupWifiData();

void setup() {
  // put your setup code here, to run once:
  Serial.begin(115200);
  pinMode(2, OUTPUT);
  digitalWrite(2, not digitalRead(2));
  delay(1000);
  digitalWrite(2, not digitalRead(2));
  delay(1000);
  EEPROM.begin(512);
  if(EEPROM.read(511) != 0b01010101){
    // Start Serial comunication for setup.
    Serial.println("Serial");
    setupWifiData();
  } else {
    // Start the wifi protocol comunication.
    Serial.println("Wifi") ;
  }

  EEPROM.end();

}

void loop() {
  // put your main code here, to run repeatedly:
}

void setupWifiData(){
  while(1){
    if(Serial.available()){
      digitalWrite(2, not digitalRead(2));
      Serial.println(Serial.readStringUntil('%'));
    }
  }
}

void EEPROM_writeSring(int startIndex, String data){
  char tmp[50];
  data.toCharArray(tmp, 50);
  int i = startIndex;
  for(;i<50; i++){
    EEPROM.write(startIndex+i, tmp[i]);
  }
  EEPROM.write(startIndex+i, 0xFF);
  EEPROM.write(511, 0b01010101);
  EEPROM.commit();
  ESP.restart();
}
