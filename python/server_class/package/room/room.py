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

    @staticmethod
    def get():
        if Room.__instance is None:
            Room()
        return Room.__instance

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


class _Room:

    class __Room:
        def __init__(self, name):
            self.__name = name
            self.__id_allocator = IdAllocator()
            self.__module = []

        def append_module(self, module_to_add):
            if not isinstance(module_to_add, Module):
                raise Exception("Room module accept only module based element")
            module_to_add.Identifier = self.__id_allocator.allocate()
            self.__module.append(module_to_add)

        def append_light(self, module, light_type, name=None):
            if light_type not in settings.LIGHT_TYPE:
                raise TypeError("Invalid light type. Must be one of "+", ".join(settings.LIGHT_TYPE.keys()))
            module = self.__module[self.__module.index(module)]

            module.append_light(settings.LIGHT_TYPE[light_type](name))

        def retrieve_light(self, module, light):
            module = self.__module[self.__module.index(module)]
            module.retrieve_light(light)

        def get_name(self):
            return self.__name
        Name = property(get_name)
    instance = None

    def __new__(cls, *args, **kwargs):
        if not Room.instance:
            Room.instance = Room.__Room(args[0])
        return Room.instance

    def __getattr__(self, attr):
        return getattr(self.instance, attr)

    def __setattr__(self, attr, val):
        return setattr(self.instance, attr, val)


if __name__ == "__main__":
    pass
