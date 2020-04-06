import package.server.httpserver as http_server
import package.server.socketserver as socket_server
import package.room.room as room

import threading
import cherrypy
import utils


class Main:

    def __init__(self):
        data = utils.Utils.get_data()
        for module, keys in data.items():
            room.Room.get().append_module(keys["data"]["type"], module)
            for light_name in keys["light"]:
                print(keys["light"][light_name])
                room.Room.get().append_light(module, keys["light"][light_name]["type"], light_name, keys["light"][light_name]["pin"])

        threading.Thread(target=self.http_server_thread).start()
        threading.Thread(target=self.socket_server_thread).start()

    def http_server_thread(self):
        cherrypy.config.update("server.conf")
        cherrypy.quickstart(http_server.HttpServer())

    def socket_server_thread(self):
        s_server = socket_server.SocketServer()
        s_server.run()


if __name__ == "__main__":
    Main()
