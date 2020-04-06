from package.jsonifier.jsonifier import Jsonifier
from utils import Utils


class Light:

    def __init__(self, name, value, pin):
        self.__pin = pin
        self.__name = name
        self._jsonifier = Jsonifier()
        self._value = value
        self._jsonifier.success("LIGHT_ADDED")

    def save_data(self, value):
        Utils.save_data({self.__name: value})

    def __eq__(self, other):
        return self.__name == other

    def __str__(self):
        return self.__name

    @staticmethod
    def get_child():
        return Light.__subclasses__()

    def switch_on(self):
        raise NotImplementedError

    def switch_off(self):
        raise NotImplementedError

    def get_value(self):
        return self._value

    def set_value(self, value):
        self._value = value

    value = property(get_value, set_value)

    def set_pin(self, pin_to_set):
        self.__pin = pin_to_set

    def get_pin(self):
        return self.__pin

    pin = property(get_pin, set_pin)

    def get_name(self):
        return self.__name
    name = property(get_name)

    def get(self):
        return self._jsonifier.get()

    def jsonify(self):
        jsonifier = Jsonifier()
        jsonifier.data({"name": self.__name, "value": self._value, "pin": self.__pin})
        return jsonifier.get()
