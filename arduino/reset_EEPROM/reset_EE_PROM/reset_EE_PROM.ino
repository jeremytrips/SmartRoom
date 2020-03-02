#include <EEPROM.h>
void setup() {
  // put your setup code here, to run once:
  EEPROM.begin(512);
  EEPROM.write(511, 0x00);
  EEPROM.commit();
  for(int i = 0 ;i<512; i++){
    EEPROM.write(i, 0x00);
  }
  EEPROM.commit();
}

void loop() {
  // put your main code here, to run repeatedly:

}
