import serial
import serial.tools.list_ports as ls_port


class SerialCommunication(serial.Serial):

    def __init__(self, port=None):
        super(SerialCommunication, self).__init__()
        self.baudrate = 115200
        self.read_until('%')
        self._port = port

    @staticmethod
    def list_port(self):
        a = ls_port.comports()
        return a

    def port(self, port):
        self._port = port
    port = property(None, port)

    def send(self, data):
        if not self.is_open:
            return -1
        self.send(data)


if __name__=="__main__":
    s = SerialCommunication("COM3")
    while 1:
        a = input("> ")
        s.send(a)
