from light import Light

class TorLight(Light):

    def __init__(self, pin, name, value=0):
        self.__value = value
        self.__old_value = self.__value
        super().__init__(pin, name)
        

    def set_value(self, value):
        self.__old_value = self.__value
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

if __name__ == "__main__":
    a = TorLight(1, "coucou")
    print(a.__dict__())