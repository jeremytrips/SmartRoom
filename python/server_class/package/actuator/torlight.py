from package.actuator.light import Light


class TorLight(Light):
    numberOfLight = 0

    def __init__(self, name=None, value=0):
        if name is None:
            TorLight.numberOfLight += 1
            name = f"Tor light {TorLight.numberOfLight}"
        self.__value = value
        super().__init__(name)

    def toggle(self, data):
        self.__value = data[self.get_name()]

    def set_value(self, value):
        if not isinstance(value, int):
            raise AttributeError("TorLight value attribute must be a bool.")
        self.save_data(self.__value)
        if value < 0:
            self.__value = 0
        elif value > 1:
            self.__value = 1
        else:
            self.__value = value

    def get_value(self):
        return self.__value
    
    Value = property(get_value, set_value)

    def __dict__(self):
        temp = super().__dict__()
        temp["value"] = self.__value
        return temp


if __name__ == "__main__":
    pass