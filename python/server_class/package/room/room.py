from package.allocator.idallocator import IdAllocator
from package.module.esp32 import Module
from package.singelton.singelton import Singleton
from package.jsonifier.jsonifier import Jsonifier

import settings

"""
Singleton
"""


@Singleton
class Room:

    def __init__(self):
        self.__name = "name"
        self.__id_allocator = IdAllocator()
        self.__modules = []
        self.__jsonifier = Jsonifier()

    def jsonify(self):
        a = Jsonifier()
        temp = dict()
        temp["name"] = self.__name
        for module in self.__modules:
            temp[module.name] = module.jsonify()
        return temp

    def switch_off(self):
        for module in self.__modules:
            module.switch_off()
        return self.jsonify()

    def switch_on(self):
        for module in self.__modules:
            module.switch_on()
        return self.jsonify()

    def append_module(self, module_to_add):
        if not isinstance(module_to_add, Module):
            raise Exception("Room module accept only module based element")
        module_to_add.identifier = self.__id_allocator.allocate()
        self.__modules.append(module_to_add)
        return module_to_add.jsonify()

    def remove_module(self, module_to_remove):
        if not isinstance(module_to_remove, Module):
            raise Exception("Room module accept only module based element")
        module_to_remove.identifier = self.__id_allocator.allocate()
        self.__modules.remove(module_to_remove)
        return {"MODULE_REMOVED": module_to_remove}

    def append_light(self, module, light_type, name=None):
        if light_type not in settings.LIGHT_TYPE:
            raise TypeError("Invalid light type. Must be one of " + ", ".join(settings.LIGHT_TYPE.keys()))
        module = self.__get_module(module)
        return module.append_light(settings.LIGHT_TYPE[light_type](name))

    def retrieve_light(self, mod, light=None):
        module = self.__get_module(mod)
        if light is None:
            return "STILL TO DO"  # TODO
        return module.retrieve_light(light).jsonify()

    def set_light(self, mod, light, value):
        module = self.__get_module(mod)
        return module.set_light(light, value)

    def __get_module(self, module):
        if module not in self.__modules:
            self.__jsonifier.error({"MODULE_DO_NOT_EXIST"})
            return
        return self.__modules[self.__modules.index(module)]

    def get_name(self):
        return self.__name

    def set_name(self, name):
        self.__name = name

    Name = property(get_name, set_name)


if __name__ == "__main__":
    pass
