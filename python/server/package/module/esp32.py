from package.module.module import Module
from package.actuator.light import Light
from package.jsonifier.jsonifier import Jsonifier

'''
ESP32
=====

The esp32 class provides an interface for the actual ESP32 device.
'''


class Esp32(Module):

    def __init__(self, name):
        super().__init__(16, 33, name)

    def append_light(self, light_to_add):
        """
        Add light to the module.
        :param light_to_add:
        :return:
        """
        if not isinstance(light_to_add, Light):
            self._jsonifier.error("SOFTWARE_ERROR")
            return self.get()
        if light_to_add in self._lights:
            self._jsonifier.error("LIGHT_ALREADY_EXIST")
            return self.get()
        light_to_add.pin = self._allocator.allocate()
        self._lights.append(light_to_add)
        self._jsonifier += light_to_add.jsonify()
        return self.get()
    
    def retrieve_light(self, light_name):
        """
        Retrieve light data from the module
        :param light_name:
        :return:
        """
        if light_name not in self._lights:
            self._jsonifier.error(["LIGHT_DONT_EXIST", light_name])
            return self.get()
        light = self._lights[self._lights.index(light_name)]
        self._jsonifier += light.jsonify()
        return self.get()

    def remove_light(self, light_to_remove):
        """
        Remove light from the module
        :param light_to_remove:
        :return:
        """
        if not isinstance(light_to_remove, Light):
            raise Exception("Module light accept only Light base element")
        if light_to_remove not in self._lights:
            raise Exception(f"You tried to remove a {light_to_remove} that is not in {self._name} lights.")
        index = self._lights.index(light_to_remove)
        self._allocator.deallocate(index)
        self._lights.remove(light_to_remove)

    def set_light(self, light_to_set, value):
        """
        Set the value of the lamp.
        :param light_to_set:
        :param value:
        :return:
        """
        if light_to_set not in self._lights:
            self._jsonifier.error({"LIGHT_DONT_EXIST_ERROR"})
            return
        for light in self._lights:
            if light == light_to_set:
                light.Value = value
                self._jsonifier += light.jsonify()
                return self.get()


if __name__ == "__main__":
    pass
