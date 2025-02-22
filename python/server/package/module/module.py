from package.allocator.pinallocator import PinAllocator
from package.jsonifier.jsonifier import Jsonifier
from utils import Utils

import copy


class Module:
    number_of_module = 0

    def __init__(self, start_index, end_index, name=None):
        if name is None:
            Module.number_of_module += 1
            name = f"Module {Module.number_of_module}"
        self._allocator = PinAllocator(start_index, end_index)
        self._name = name
        self._identifier = -1
        self._lights = []
        self._jsonifier = Jsonifier()
        self._jsonifier.success("MODULE_ADDED")
        self.__attributed = False
        self._change_list = list()

    def get_pin_allocator(self):
        return self._allocator.jsonify()

    def set_used_pin(self, pin_id=None):
        if pin_id is not None:
            self._allocator.set_used(pin_id)

    def has_change(self):
        return len(self._change_list) > 0

    def get_changes(self):
        temp = {self._name: copy.deepcopy(self._change_list)}
        self._change_list.clear()
        return temp

    def get_attributed(self):
        return self.__attributed

    def set_attributed(self, value):
        self.__attributed = value

    attributed = property(get_attributed, set_attributed)

    def get(self):
        return self._jsonifier.get()

    def jsonify(self):
        jsonifier = Jsonifier()
        temp_dict = dict()
        temp_dict["data"] = {"name": self._name}
        for light in self._lights:
            temp_dict[str(light)] = light.jsonify()
        jsonifier.data(temp_dict)
        return jsonifier.get()

    def switch_on(self):
        for light in self._lights:
            light.switch_on()
            self._jsonifier += light.jsonify()
            self._change_list.append(("s", light))

    def switch_off(self):
        for light in self._lights:
            light.switch_off()
            self._jsonifier.data(light.jsonify())
            self._change_list.append(("s", light))

    def get_identifier(self):
        return self._identifier

    def set_identifier(self, identifier):
        self._identifier = identifier

    identifier = property(get_identifier, set_identifier)

    def get_name(self):
        return self._name

    def set_name(self, name):
        self._name = name

    name = property(get_name, set_name)

    def _get_light(self, light):
        return self._lights[self._lights.index(light)]

    def __str__(self):
        return f"{self._name}"

    def __repr__(self):
        return self._name

    def __eq__(self, other):
        return self._name == other


if __name__ == "__main__":
    a = Module(0, 25)
    print(a.jsonify())
