from package.module.module import Module
from package.actuator.light import Light
import utils

'''
ESP32
=====

The esp32 class provides an interface for the actual ESP32 device.
'''


class Esp32(Module):

    def __init__(self, name):
        super().__init__(16, 32, name)

    @classmethod
    def get_type(cls):
        return "esp32"

    def append_light(self, light_to_add):
        """
        Add light to the module.
        :param pin:
        :param light_to_add:
        :return:
        """
        if not isinstance(light_to_add, Light):
            self._jsonifier.error("SOFTWARE_ERROR")
            return self.get()
        if light_to_add in self._lights:
            self._jsonifier.error("LIGHT_ALREADY_EXIST")
            return self.get()
        if light_to_add.pin is None:
            pin_allocator = self._allocator.allocate()
            if "error" in pin_allocator.keys():
                return pin_allocator
            light_to_add.pin = pin_allocator["data"][0]["pin"]
        self._lights.append(light_to_add)
        self._jsonifier += light_to_add.jsonify()
        self._change_list.append(("c", light_to_add))
        utils.Utils.save_light(self._name, light_to_add)
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
        if light_to_remove not in self._lights:
            raise Exception(f"You tried to remove a {light_to_remove} that is not in {self._name} lights.")
        index = self._lights.index(light_to_remove)
        self._allocator.deallocate(index)
        self._lights.remove(light_to_remove)
        utils.Utils.delete_light(self._name, light_to_remove)
        self._jsonifier.success("LIGHT_REMOVED")
        return self.get()

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
                self._change_list.append(("s", light.jsonify()["data"][0]))
                return self.get()


if __name__ == "__main__":
    pass
