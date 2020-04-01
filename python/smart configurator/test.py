import serialcom
import time
import serial

a = serialcom.SerialCom()
a.port = "COM12"
while 1:
    a.send(b"coucoucommbetd")
    time.sleep(0.5)