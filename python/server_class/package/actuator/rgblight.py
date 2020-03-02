from light import Light


class RgbLight(Light):

    def __init__(self, pin, name, value=[0, 0, 0]):
        self.__value = value
        self.__old_value = self.__value
        super().__init__(pin, name)
        
    def set_value(self, value):
        self.__old_value = self.__value
        for i in range(len(value)):
            print(self.value[i])
            if value[i] < 0:
                self.__value[i] = 0
            elif value[i] > 255:
                self.__value[i] = 255
            else:
                self.__value[i] = value[i]

    def get_value(self):
        return self.__value

    value = property(get_value, set_value)

    def __dict__(self):
        return {
            "pin": self.pin,
            "name": self.name, 
            "value": self.__value
        }

if __name__ == "__main__":
    a = RgbLight(1, "coucou")
    a.value = [123, 2123, 0]
    print(a.__dict__())