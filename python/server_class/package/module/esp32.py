from .module import Module
a = list()
a.index


class Esp32(Module):

    def __init__(self, name):
        super().__init__(name, 16, 33)
        self.light = []

    def append_light(self, light):
        self.light.append(light)
    
    def retrieve_light(self, light_name):
        return self.light[self.light.index(light_name)]