from package.actuator.light import Light


class TorLight(Light):
    numberOfLight = 0

    def __init__(self, name=None, value=0):
        if name is None:
            TorLight.numberOfLight += 1
            name = f"Tor light {TorLight.numberOfLight}"
        self.__value = value
        self.__old_value = self.__value
        super().__init__(name)

    def set_value(self, value):
        if not isinstance(value, bool):
            raise AttributeError("TorLight value attribute must be a bool.")
        self.__old_value = self.__value
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