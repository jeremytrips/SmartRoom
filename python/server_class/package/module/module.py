from package.allocator.pinallocator import PinAllocator
from package.jsonifier.jsonifier import Jsonifier
from utils import Utils


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

    def jsonify(self):
        self._jsonifier.data({"name": self._name})
        for elem in self._lights:
            self._jsonifier.data({elem.name: elem.jsonify()})
        return

    def switch_on(self):
        data = Utils.get_data()
        for light in self._lights:
            light.toggle(data)

    def switch_off(self):
        for light in self._lights:
            light.Value = 0

    def allocate(self):
        return self._allocator.allocate()

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
        return f"{self._name} at {id(self)}"

    def __eq__(self, other):
        return self._name == other


if __name__ == "__main__":
    a = Module(0, 25)
    print(a.jsonify())
