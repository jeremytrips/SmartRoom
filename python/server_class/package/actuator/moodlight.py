from package.actuator.light import Light


class MoodLight(Light):
    numberOfLight = 0

    def __init__(self, name, value=0):
        if name is None:
            MoodLight.numberOfLight += 1
            name = f"Mood light {MoodLight.numberOfLight}"
        self.__value = value
        super().__init__(name)

    def toggle(self, data):
        self.__value = data[self.get_name()]

    def set_value(self, value):
        if not isinstance(value, int):
            raise AttributeError("MoodLight value attribute must be an int.")
        self.save_data(self.__value)
        if value < 0:
            self.__value = 0
        elif value > 255:
            self.__value = 255
        else:
            self.__value = value

    def get_value(self):
        return self.__value

    Value = property(get_value, set_value)

    def __dict__(self):
        temp = super().__dict__()
        temp["value"] = self.__value
        return temp
