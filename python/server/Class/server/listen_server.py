from http.server import BaseHTTPRequestHandler,HTTPServer
import json

PORT_NUMBER = 1515

class ListenServer(BaseHTTPRequestHandler):

	def do_GET(self):
		url = self.path.split('/')
		url.pop(0)
		self.handle_data(url)

	def write(self, data):
		self.wfile.write(f"{json.dumps(data)}".encode())

	def handle_data(self, data):
		if data[0] == "set":
			pass
		elif data[0] == "get":
			pass
		else:
			error = {"error": f"Error action invalid '{data[0]}'"}
			self.write(error)

if __name__ == "__main__":
	try:

		server = HTTPServer(('', PORT_NUMBER), myHandler)
		print('Started httpserver on port ' , PORT_NUMBER)
		server.serve_forever()

	except KeyboardInterrupt:
		print('^C received, shutting down the web server')
		server.socket.close()
		