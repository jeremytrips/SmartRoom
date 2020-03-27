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
        self.__value = value
        super().__init__(name)

    def toggle(self, data):
        self.__value = data[self.get_name()]

    def set_value(self, value):
        if isinstance(value, int):
            value = [value, value, value]
            # warnings.warn("set_value should have a list attribute not an int", Warning)
        if not isinstance(value, list):
            raise AttributeError("RgbLight value attribute must be a list of int.")
        self.save_data(self.__value)
        for i in range(len(value)):
            if value[i] < 0:
                self.__value[i] = 0
            elif value[i] > 255:
                self.__value[i] = 255
            else:
                self.__value[i] = value[i]

    def get_value(self):
        return self.__value

    Value = property(get_value, set_value)

    def __dict__(self):
        temp = super().__dict__()
        temp["value"] = self.__value
        return temp


if __name__ == "__main__":
    pass
