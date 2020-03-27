
class Light:

    def __init__(self, name):
        self.__pin = -1
        self.__name = name

    def __eq__(self, other):
        return self.__name == other

    def __str__(self):
        return self.__name

    def set_pin(self, pin_to_set):
        self.__pin = pin_to_set

    def get_pin(self):
        return self.__pin

    Pin = property(get_pin, set_pin)

    def get_name(self):
        return self.name
    Name = property(get_name)

    def __dict__(self):
        return {"pin": self.pin, "name": self.name}
