from package.actuator.light import Light


class TorLight(Light):
    numberOfLight = 0

    def __init__(self, name, pin=None, value=0):
        if name is None:
            TorLight.numberOfLight += 1
            name = f"Tor light {TorLight.numberOfLight}"
        super().__init__(name, value, pin)
        self._jsonifier.success("MODULE_ADDED")

    @classmethod
    def get_type(cls):
        return "TOR"

    def toggle(self, data):
        self._value = data[self.get_name()]

    def switch_on(self):
        self._value = 1

    def switch_off(self):
        self.save_data(self._value)
        self._value = 0

    def set_value(self, value):
        if not isinstance(value, int):
            raise AttributeError("TorLight value attribute must be a bool.")
        self.save_data(self._value)
        if value < 0:
            self._value = 0
        elif value > 1:
            self._value = 1
        else:
            self._value = value

    def get_value(self):
        return self._value

    Value = property(get_value, set_value)


if __name__ == "__main__":
    pass
