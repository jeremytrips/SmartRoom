from package.module.module import Module
from package.actuator.light import Light
from package.jsonifier.jsonifier import Jsonifier


class Esp32(Module):

    def __init__(self, name):
        super().__init__(16, 33, name)

    def append_light(self, light_to_add):
        """
        Add light to the module.
        :param light_to_add:
        :return:
        """
        if light_to_add in self._lights:
            self._jsonifier.error("LIGHT_ALREADY_EXIST")
            return
        light_to_add.pin = self._allocator.allocate()
        self._lights.append(light_to_add)
        return
    
    def retrieve_light(self, light_name):
        """
        Retrieve light data from the module
        :param light_name:
        :return:
        """
        if light_name not in self._lights:
            self._jsonifier.error({"error": ["LIGHT_DONT_EXIST", light_name]})
            return
        light = self._lights[self._lights.index(light_name)]
        return light.jsonify()

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
                return light.jsonify()


if __name__ == "__main__":
    pass
