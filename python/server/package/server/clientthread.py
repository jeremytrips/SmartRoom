import socket
import time

import socket, threading


class ClientThread(threading.Thread):

    def __init__(self,clientAddress, clientsocket, identifier):
        threading.Thread.__init__(self)
        self.csocket = clientsocket
        self.clientAddress = clientAddress
        self.identifier = identifier
        print (f"New connection added: {self.clientAddress} with id: {self.identifier}")

    def run(self):
        print ("Connection from : ", self.clientAddress)
        msg = ''
        while True:
            data = self.csocket.recv(64)
            msg = data.decode()
            if msg=='bye':
              break
            elif msg != "":
                
                msg = ""
            self.csocket.send(bytes(msg,'UTF-8'))
        print ("Client at ", self.clientAddress , " disconnected...")

    def send(self, data):
        self.csocket.send(data.encode('utf-8'))

    def __repr__(self):
        self.identifier

    def __str__(self):
        self.identifier