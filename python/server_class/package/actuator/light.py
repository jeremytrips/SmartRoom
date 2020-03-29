from package.jsonifier.jsonifier import Jsonifier
from utils import Utils


class Light:

    def __init__(self, name):
        self.__pin = -1
        self.__name = name
        self._jsonifier = Jsonifier()
        self._value = None

    def save_data(self, value):
        Utils.save_data({self.__name: value})

    def __eq__(self, other):
        return self.__name == other

    def __str__(self):
        return self.__name

    def set_pin(self, pin_to_set):
        self.__pin = pin_to_set

    def get_pin(self):
        return self.__pin

    pin = property(get_pin, set_pin)

    def get_name(self):
        return self.__name
    name = property(get_name)

    def jsonify(self):
        self._jsonifier.data({"name": self.__name, "value": self._value})
        self._jsonifier.get()
