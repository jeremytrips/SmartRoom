import serial
import serial.tools.list_ports as ls_port
import threading
import time


class SerialCom:

    def __init__(self):
        self.port_com = serial.Serial(baudrate=115200, timeout=0.1, write_timeout=0.1)
        self.port = -1
        self.port_running = False
        self.listen_thread = threading.Thread(target=self.receive)
        self.write_thread = threading.Thread(target=self.send)

    @staticmethod
    def list_port():
        com = ls_port.comports()
        rt_list = []
        for port in com:
            tmp = port.description.index("COM")
            rt_list.append(str(port.description)[tmp:-1])
        return rt_list

    def port(self, port):
        if port == -1:
            print("closing")
            self.port_running = False
            time.sleep(0.1)
            self.port_com.close()
            return
        self.port_com.port = port
        self.port_com.open()
        self.port_running = True
        self.listen_thread.run()
        self.write_thread.run()
    port = property(None, port)

    def send(self, data=None, action=None):
        to_send = data + " " * (48 - len(data))
        to_send += action
        to_send += "%"
        self.port_com.write(to_send)

    def receive(self):
        while self.port_running:
            if not self.port_com.is_open:
                pass
            elif not self.port_com.in_waiting:
                pass
            else:
                print(self.port_com.read(self.port_com.in_waiting).decode())
            time.sleep(0.1)


if __name__ == "__main__":
    def format_string(data, action):
        to_send = data + " " * (48 - len(data))
        to_send += action
        to_send += "%"
        print(to_send)

    format_string("netis_C30DB3", 's')
    format_string("password", 'p')

# netis_C30DB3                                    s%
# password                                        p%

