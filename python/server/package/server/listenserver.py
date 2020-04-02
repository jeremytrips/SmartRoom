from http.server import BaseHTTPRequestHandler,HTTPServer
from package.room.room import Room
import json
import settings

# module/add/module_type/module_name				=> room.append_module(module_type, (module_name)):
# module/remove/module_name							=> room.remove_module(module_name)

# light/get/module_name/light						=> room.retrieve_light(module_name, (light))
# light/set/module_name/light/value					=> room.set_light(module_name, light_name, value)
# light/set/on										=> room.switch_on()
# light/set/off 									=> room.switch_off()
# light/add/module_name/light_type/light_name		=> room.append_light(module_name, light_type, (light_name))
# light/remove/module_name/light_name


class ListenServer(BaseHTTPRequestHandler):

	def do_GET(self):
		url = self.path.split('/')
		url.pop(0)
		print(url)
		if url[0] == "light":
			self.handle_light(url.pop(0))
		self.handle_data(url)

	def write(self, data):
		self.wfile.write(f"{json.dumps(data)}".encode())

	def handle_light(self, url):
		a = str()
		if url[0] == "on":
			a = Room.get().switch_on()
		elif url[0] == "off":
			a = Room.get().switch_off()

		Room.get().handle_light()

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
