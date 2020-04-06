from package.server.clientthread import ClientThread
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
    
    def run(self):
        self.server_thread.start()

    def run_server(self):
        self.sock.bind(("0.0.0.0", 8090))
        identifier = -1
        while True:
            self.sock.listen(10)
            print("Socket server listening and waiting for connection.")
            client_sock, client_address = self.sock.accept()
            print("incoming connection")
            identifier = client_sock.recv(32).decode()
            if identifier == "no_name":
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

    def send(self, data):
        for elem in self.client:
            elem.send(data)


if __name__ == "__main__":
    pass
