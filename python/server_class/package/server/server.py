from .clientthread import ClientThread
from .listenserver import ListenServer
from http.server import BaseHTTPRequestHandler,HTTPServer

import socket
import threading

LOCALHOST = "0.0.0.0"
SOCKET_PORT = 8090
LISTEN_PORT = 8091

class Server():

    def __init__(self):
        # super().__init__()
        self.net = HTTPServer((LOCALHOST, LISTEN_PORT), ListenServer)
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.port = SOCKET_PORT
        self.host = LOCALHOST
        self.client = list()
        self.server_thread = threading.Thread(target=self.run_server)
    
    def run(self):

        self.server_thread.start()
        self.net.serve_forever()

    def run_server(self):
        self.sock.bind((self.host, self.port))
        identifier = -1
        while(True):
            self.sock.listen(10)
            clientsock, clientAddress = self.sock.accept()
            print("incoming connection")
            identifier = clientsock.recv(32).decode()
            print(f"{identifier} is connected")

            newthread = ClientThread(clientAddress, clientsock, identifier)
            self.client.append(newthread)
            newthread.start()

    def send(self, data, identifier):     
        for elem in self.client:
            if identifier == 0:  
                elem.send(data)
            else:
                if self.identifier == str(elem):
                    elem.send(data)


if __name__ == "__main__":
    s = SocketServer()
    s.run()  