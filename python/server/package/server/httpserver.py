import package.room.room as r

# module/add/module_type/module_name				=> room.append_module(module_type, (module_name)):
# module/get/module_name							=> room.retrieve_module(module_name)
# module/remove/module_name							=> room.remove_module(module_name)

# light/get/module_name/light						=> room.retrieve_light(module_name, (light))
# light/set/module_name/light/value					=> room.set_light(module_name, light_name, value)
# light/action/on										=> room.switch_on()
# light/action/off 									=> room.switch_off()
# light/add/module_name/light_type/light_name		=> room.append_light(module_name, light_type, (light_name))
# light/remove/module_name/light_name

import cherrypy


class HttpServer:

	@cherrypy.expose()
	def light(self, *args):
		url = self.__format_url(args)
		if url[0] == "action":
			# [action, action_type]
			return str(r.Room.get().get_action()[url[1]]())
		if url[0] == "get":
			# [get, module_name, light_name]
			return str(r.Room.get().retrieve_light(url[1], url[2]))
		if url[0] == "set":
			# [set, module_name, light_name, value]
			return str(r.Room.get().set_light(url[1], url[2], url[3]))
		if url[0] == "add":
			# [add, light_type, light_name]
			return str(r.Room.get().append_light(url[1], url[2], url[3]))
		if url[0] == "remove":
			# [remove, module_name, light_name]
			return str(r.Room.get().remove_light(url[1], url[2]))

	@cherrypy.expose()
	def module(self, *args):
		url = self.__format_url(args)
		if url[0] == "add":
			# [action, type, name]
			room = r.Room.get()
			return str(room.append_module(url[1], url[2]))
		if url[0] == "retrieve":
			# [action, name]
			return str(r.Room.get().retrieve_module(url[1]))
		if url[0] == "remove":
			# [action, name]
			return str(r.Room.get().remove_module(url[1]))

	@staticmethod
	def __format_url(data):
		data = list(data)
		while len(data) < 5:
			data.append(None)
		return data


if __name__ == '__main__':
	pass