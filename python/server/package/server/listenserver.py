from http.server import BaseHTTPRequestHandler,HTTPServer
from package.room.room import Room
import json
import settings

# action_type/module_name/light_name(/value)
# get/module_name 									=> room.retrieve_light(module_name)
# get/module_name/light_name 						=> room.retrieve_light(module_name, light_name)
# on/												=> room.switch_on()
# off/ 												=> room.switch_off()
# set/module_name/light_name/value					=> room.set_light(module_name, light_name, value)


class ListenServer(BaseHTTPRequestHandler):

	def do_GET(self):
		url = self.path.split('/')
		url.pop(0)
		print(url)
		self.handle_data(url)

	def write(self, data):
		self.wfile.write(f"{json.dumps(data)}".encode())

	def handle_data(self, data):
		room = Room.get()
		if data[0] == "set":
			pass
		elif data[0] == "get":
			self.write(room)
			if data[1] == "module":
				self.write("")
			else:
				error = {"error": f"Error action invalid '{data[1]}'"}
				self.write(error)
		else:
			error = {"error": f"Error action invalid '{data[0]}'"}
			self.write(error)


if __name__ == "__main__":
	try:
		server = HTTPServer(('', settings.PORT_NUMBER), ListenServer)
		print('Started httpserver on port ', settings.PORT_NUMBER)
		server.serve_forever()

	except KeyboardInterrupt:
		print('^C received, shutting down the web server')
		server.socket.close()
