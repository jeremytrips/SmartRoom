from light import Light

class MoodLight(Light):

    def __init__(self, pin, name, value=0):
        self.__value = value
        self.__old_value = self.__value
        super().__init__(pin, name)
        
    def set_value(self, value):
        self.__old_value = self.__value
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
        return {
            "pin": self.pin,
            "name": self.name, 
            "value": self.__value
        }