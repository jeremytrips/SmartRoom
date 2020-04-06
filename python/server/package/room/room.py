from package.allocator.idallocator import IdAllocator
import utils
from package.singelton.singelton import Singleton
from package.jsonifier.jsonifier import Jsonifier

import settings


@Singleton
class Room:

    def __init__(self):
        self.__name = "name"
        self.__id_allocator = IdAllocator()
        self.__modules = []
        self.__jsonifier = Jsonifier()

    def get_not_attributed(self):
        not_attributed = list()
        for mod in self.__modules:
            if not mod.attributed:
                not_attributed.append(mod)
        return not_attributed

    def get_attributed(self, module):
        print("mab")
        print(self.__modules)
        module = self.__get_module(module)
        print(module)
        return module.attributed

    def set_attributed(self, mod, value):
        module = self.__get_module(mod)
        module.set_attributed(value)

    def get_action(self):
        return {"on": self.switch_on, "off": self.switch_off}

    def get_modules(self):
        print(f"Get module: {id(self)}")
        return self.__modules

    def append_module(self, module_type, module_name=None):
        """

        :param module_type:
        :param module_name:
        :return:
        """
        print(f"append module: {id(self)}")
        if module_type not in settings.MODULE_TYPE.keys():
            self.__jsonifier.error("NOT_MODULE_ERROR")
            return self.get()
        if len(self.__modules) >= 10:
            self.__jsonifier.error("MAX_MODULE_ERROR")
            return self.get()
        if module_name in self.__modules:
            self.__jsonifier.error("MODULE_ALREADY_EXIST_ERROR")
            return self.get()
        module_to_add = settings.MODULE_TYPE[module_type](module_name)
        module_to_add.identifier = self.__id_allocator.allocate()
        utils.Utils.save_module(module_type, module_to_add)
        self.__modules.append(module_to_add)
        self.__jsonifier += module_to_add.get()
        return self.get()

    def retrieve_module(self, module_name):
        """

        :param module_name:
        :return:
        """
        if module_name not in self.__modules:
            self.__jsonifier.error("MODULE_DONT_EXIST_ERROR")
            return self.get()
        module = self.__get_module(module_name)
        return module.jsonify()

    def remove_module(self, module_name):
        if module_name not in self.__modules:
            self.__jsonifier.error("MODULE_DONT_EXIST_ERROR")
            return self.get()
        module = self.__get_module(module_name)
        self.__id_allocator.deallocate(module.identifier)
        self.__modules.remove(module)
        utils.Utils.delete_module(module_name)
        self.__jsonifier.success("MODULE_REMOVED")
        return self.__jsonifier.get()

    def get(self):
        return self.__jsonifier.get()

    def jsonify(self):
        jsonifier = Jsonifier()
        for module in self.__modules:
            jsonifier += module.jsonify()
        return jsonifier.get()

    def switch_off(self):
        for module in self.__modules:
            module.switch_off()
            self.__jsonifier += module.jsonify()
        return self.get()

    def switch_on(self):
        for module in self.__modules:
            module.switch_on()
            self.__jsonifier += module.jsonify()
        return self.get()

    def append_light(self, mod, light_type, name=None, pin=None):
        if light_type not in settings.LIGHT_TYPE:
            self.__jsonifier.error(["LIGHT_TYPE_DO_NOT_EXIST"])
            return self.get()
        if mod not in self.__modules:
            self.__jsonifier.error("MODULE_DO_NOT_EXIST")
            return self.get()
        module = self.__get_module(mod)
        light = settings.LIGHT_TYPE[light_type](name, pin)
        print(light)
        self.__jsonifier += module.append_light(light)
        return self.get()

    def retrieve_light(self, mod, light=None):
        if mod not in self.__modules:
            self.__jsonifier.error("MODULE_DO_NOT_EXIST")
            return self.get()
        module = self.__get_module(mod)
        if light is None:
            self.__jsonifier += module.jsonify()
            return self.get()
        self.__jsonifier += module.retrieve_light(light)
        return self.get()

    def remove_light(self, module_light, light_name):
        module = self.__get_module(module_light)
        self.__jsonifier += module.remove_light(light_name)
        return self.get()

    def set_light(self, mod, light, value):
        module = self.__get_module(mod)
        self.__jsonifier += module.set_light(light, value)
        return self.get()

    def __get_module(self, module):
        if module not in self.__modules:
            self.__jsonifier.error({"MODULE_DO_NOT_EXIST"})
            return self.get()
        return self.__modules[self.__modules.index(module)]

    def get_name(self):
        return self.__name

    def set_name(self, name):
        self.__name = name

    name = property(get_name, set_name)


if __name__ == "__main__":
    pass
