import socket
from package.room.room import Room


import threading
import json
from package.server.server import Server

def http_server():
        server = HTTPServer(('', LISTEN_PORT), ListenServer)
        print('Started httpserver on port ' , LISTEN_PORT)
        server.serve_forever()

# def socket_server():
#     sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#     sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
#     sock.bind((LOCALHOST, SOCKET_PORT))

#     print("Waiting for client request..")
#     while True:
#         sock.listen(10)
#         clientsock, clientAddress = sock.accept()

#         newthread = ClientThread(clientAddress, clientsock)
#         module
#         newthread.start()


if __name__ == "__main__":
    room = Room()
    Server(room).run()
    