import serial
import serial.tools.list_ports as ls_port
import threading


class SerialCommunication():

    def __init__(self):
        self.port_com = serial.Serial(baudrate=115200, timeout=0.1, write_timeout=0.1)
        self.port = -1
        self.port_running = False
        self.listen_thread = threading.Thread(target=self.receive)
        self.write_thread = threading.Thread(target=self.send)

    @staticmethod
    def list_port():
        return ls_port.comports()

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

    def send(self, data=None):
        while self.port_running:
            print("in")
            data = input('> ')
            if data == "1":
                self.port = -1
            elif not self.port_com.is_open:
                pass
            else:
                self.port_com.write(data.encode())
            time.sleep(0.01)

    def receive(self):
        while self.port_running:
            if not self.port_com.is_open:
                pass
            elif not self.port_com.in_waiting:
                pass
            else:
                print(self.port_com.read(self.port_com.in_waiting).decode())
            time.sleep(0.01)


if __name__ == "__main__":
    import time
    s = SerialCommunication()
    s.port = "COM3"

