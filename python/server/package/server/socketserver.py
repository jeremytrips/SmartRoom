from package.server.clientthread import ClientThread
import package.socketifier.socketifier as socketifier
import package.room.room as room
import socket
import threading
import time

LOCALHOST = "0.0.0.0"
SOCKET_PORT = 8090
LISTEN_PORT = 8091


class SocketServer:

    def __init__(self):
        # super().__init__()
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.client = list()
        self.server_thread = threading.Thread(target=self.run_server)
        self.send_thread = threading.Thread(target=self.send)
        self.run_bool = True
    
    def run(self):
        self.server_thread.start()
        self.send_thread.start()

    def run_server(self):
        self.sock.bind(("0.0.0.0", 8090))
        identifier = -1
        while self.run_bool:
            self.sock.listen(10)
            print("Socket server listening and waiting for connection.")
            client_sock, client_address = self.sock.accept()
            print("incoming connection")
            identifier = client_sock.recv(32).decode()
            if identifier == "no_name":
                print("Incoming connection has no identifier set."
                      "Waiting for not attributed Module from http server")
                while len(room.Room.get().get_not_attributed()) == 0:
                    time.sleep(0.01)
                a = room.Room.get().get_not_attributed()
                print(a)
                client_sock.send(f"{a[0].name}%".encode('utf-8'))
                room.Room.get().set_attributed(a[0], True)
                print(f"Identifier {a[0].name} has been attributed")
            else:
                print(f"{identifier} is connected")

            new_thread = ClientThread(client_address, client_sock, identifier)
            self.client.append(new_thread)
            new_thread.start()

    def send(self):
        while self.run_bool:
            if room.Room.get().has_change():
                data = room.Room.get().get_change()
                socketifier.Socketifier().Socketify(data)
                """module = self.client[self.__get_client(data[0])]
                module.send(data[1])"""

            time.sleep(0.001)

    def __get_client(self, module):
        return self.client.index(module)


if __name__ == "__main__":
    pass
