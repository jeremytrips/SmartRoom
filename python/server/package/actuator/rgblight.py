from package.actuator.light import Light
from utils import Utils


class RgbLight(Light):
    numberOfLight = 0

    def __init__(self, name=None, pin=None, value=None):
        if value is None:
            value = [0, 0, 0]
        if name is None:
            RgbLight.numberOfLight += 1
            name = f"RGB light {RgbLight.numberOfLight}"
        super().__init__(name, value, pin)
        self._jsonifier.success("LIGHT_ADDED")

    @classmethod
    def get_type(cls):
        return "RGB"

    def toggle(self, data):
        self._value = data[self.get_name()]

    def switch_on(self):
        self._value = [Utils.get_switch_on_value()] * 3

    def switch_off(self):
        self.save_data(self._value)
        self._value = [0] * 3

    def set_value(self, value):
        value = int(value)
        if isinstance(value, int):
            value = [value, value, value]
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


if __name__ == "__main__":
    pass
