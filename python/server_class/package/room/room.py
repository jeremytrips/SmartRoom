from package.allocator.idallocator import IdAllocator
from package.module.esp32 import Module

import settings

"""
Singleton
"""


class Room:

    def __init__(self):
        self.__name = "name"
        self.__id_allocator = IdAllocator()
        self.__module = []

    def append_module(self, module_to_add):
        if not isinstance(module_to_add, Module):
            raise Exception("Room module accept only module based element")
        module_to_add.Identifier = self.__id_allocator.allocate()
        self.__module.append(module_to_add)

    def append_light(self, module, light_type, name=None):
        if light_type not in settings.LIGHT_TYPE:
            raise TypeError("Invalid light type. Must be one of " + ", ".join(settings.LIGHT_TYPE.keys()))
        module = self.__module[self.__module.index(module)]

        module.append_light(settings.LIGHT_TYPE[light_type](name))

    def retrieve_light(self, module, light):
        module = self.__module[self.__module.index(module)]
        module.retrieve_light(light)

    def get_name(self):
        return self.__name

    Name = property(get_name)


if __name__ == "__main__":
    pass
