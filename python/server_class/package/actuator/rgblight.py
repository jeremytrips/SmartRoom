from package.actuator.light import Light
import warnings


class RgbLight(Light):
    numberOfLight = 0

    def __init__(self, name=None, value=None):
        if value is None:
            value = [0, 0, 0]
        if name is None:
            RgbLight.numberOfLight += 1
            name = f"RGB light {RgbLight.numberOfLight}"
        self._value = value
        super().__init__(name)

    def toggle(self, data):
        self._value = data[self.get_name()]

    def set_value(self, value):
        if isinstance(value, int):
            value = [value, value, value]
            # warnings.warn("set_value should have a list attribute not an int", Warning)
        if not isinstance(value, list):
            raise AttributeError("RgbLight value attribute must be a list of int.")
        self.save_data(self._value)
        for i in range(len(value)):
            if value[i] < 0:
                self._value[i] = 0
            elif value[i] > 255:
                self._value[i] = 255
            else:
                self._value[i] = value[i]

    def get_value(self):
        return self._value

    Value = property(get_value, set_value)

    def jsonify(self):
        return self._jsonifier.get()


if __name__ == "__main__":
    pass
