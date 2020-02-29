
class Light:

    def __init__(self, pin, name):
        self.pin = pin
        self.name = name

    def __dict__(self):
        return {"pin": self.pin, "name": self.name}
