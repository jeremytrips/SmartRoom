#include <EEPROM.h>
char buf[50] = {0};

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
    //printf("value: %d, factor: %f\n", tmp, factor);
    toReturn += tmp * factor;
  }
  return toReturn;
}
char ssid[50];
char password[50];
char temp[10];
char host[50];
char tmp[50];
char action;
int port = -1;
int writen = 0;

void setup() {
  // put your setup code here, to run once:
  Serial.begin(115200);
  EEPROM.begin(512);


  Serial.println(ssid);
  Serial.println(password);
  Serial.println(host);
  Serial.println(temp);
  Serial.println(arrayToInt(temp));

  Serial.println("nok");
}

void loop() {
  // put your main code here, to run repeatedly:
  if (Serial.available()) {
    String str = Serial.readStringUntil('%');
    str.toCharArray(tmp, 50);
    action = tmp[48];
    Serial.println("-----------------------------------");
    Serial.println(str);
    Serial.println(action);
    Serial.println("-----------------------------------");
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
    Serial.println("=========================================");
    EEPROM_read(ssid, 401);
    EEPROM_read(password, 451);
    EEPROM_read(host, 301);
    EEPROM_read(temp, 351);
    Serial.println(ssid);
    Serial.println(password);
    Serial.println(host);
    Serial.println(temp);
    Serial.println("=========================================");
    writen = 0;
  }
}
