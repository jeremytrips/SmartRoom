from package.allocator.pinallocator import PinAllocator
from utils import Utils


class Module:
    number_of_module = 0

    def __init__(self, start_index, end_index, name=None):
        if name is None:
            Module.number_of_module += 1
            name = f"Module {Module.number_of_module}"
        self.__allocator = PinAllocator(start_index, end_index)
        self.__name = name
        self.__identifier = -1
        self.lights = []

    def switch_on(self):
        data = Utils.get_data()
        for light in self.lights:
            light.toggle(data)

    def switch_off(self):
        for light in self.lights:
            light.Value = 0

    def __eq__(self, other):
        return self.__name == other

    def allocate(self):
        return self.__allocator.allocate()

    def get_identifier(self):
        return self.__identifier

    def set_identifier(self, identifier):
        self.__identifier = identifier

    Identifier = property(get_identifier, set_identifier)

    def get_name(self):
        return self.__name

    def set_name(self, name):
        self.__name = name

    Name = property(get_name, set_name)

    def __str__(self):
        return f"{self.__name} at {id(self)}"


if __name__ == "__main__":
    a = Module(0, 25)
    print(vars(a))