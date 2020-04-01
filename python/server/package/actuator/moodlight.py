from utils import Utils
from package.actuator.light import Light


class MoodLight(Light):
    numberOfLight = 0

    def __init__(self, name, value=0):
        if name is None:
            MoodLight.numberOfLight += 1
            name = f"Mood light {MoodLight.numberOfLight}"
        super().__init__(name, value)
        self._jsonifier.success("MODULE_ADDED")

    def toggle(self, data):
        self._value = data[self.get_name()]

    def switch_on(self):
        self._value = Utils.get_switch_on_value()

    def switch_off(self):
        self.save_data(self._value)
        self._value = 0

    def set_value(self, value):
        if not isinstance(value, int):
            raise AttributeError("MoodLight value attribute must be an int.")
        self.save_data(self._value)
        if value < 0:
            self._value = 0
        elif value > 255:
            self._value = 255
        else:
            self._value = value

    def get_value(self):
        return self._value

    Value = property(get_value, set_value)
