import serial
import serial.tools.list_ports as ls_port
import threading
import time


class SerialCom:

    def __init__(self):
        self.port_com = serial.Serial(baudrate=115200, timeout=0.5, write_timeout=0.1)
        self.port = -1
        self.port_running = False
        self.received = None

    def set_port(self, port):
        if port == -1:
            self.port_running = False
            time.sleep(0.1)
            self.port_com.close()
            return
        self.port_com.port = port
        self.port_com.open()
        self.port_running = True
    port = property(None, set_port)

    def write(self, data=None, action=None):
        if not (isinstance(data, bytes) or isinstance(data, str)):
            raise TypeError("Data must be bytes")
        if action is None:
            self.port_com.write(data)
            return
        to_send = data + " " * (48 - len(data))
        to_send += action
        to_send += "%"
        print(to_send)
        #self.port_com.write(to_send.encode())

    def receive(self):
        run = True
        self.port_com.read_all()
        i = 0
        while run:
            if not self.port_com.is_open:
                raise Exception(f"Port {self.port_com} not open")
            if i == 50:
                return -1
            if self.port_com.inWaiting():
                run = False
                return self.port_com.read_all()
            i += 1
            time.sleep(0.1)

    def close(self):
        self.port_running = False
        self.port_com.close()

    def get_received(self):
        return self.received

    @staticmethod
    def list_port():
        com = ls_port.comports()
        rt_list = []
        for port in com:
            tmp = port.description.index("COM")
            rt_list.append(str(port.description)[tmp:-1])
        return rt_list


if __name__ == "__main__":
    pass
# netis_C30DB3                                    s%
# password                                        p%
# 192.168.1.23                                    i%
# 8090                                            o%
