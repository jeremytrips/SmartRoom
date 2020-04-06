import serialcom
import time
import serial

a = serialcom.SerialCom()
# a.port = "COM12"
print(type(0b010101))
while 1:
    a.send(125)
    time.sleep(0.5)