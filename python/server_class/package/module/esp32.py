from package.module.module import Module
from package.actuator.light import Light


class Esp32(Module):

    def __init__(self, name):
        super().__init__(16, 33, name)
        self.lights = []

    def append_light(self, light_to_add):
        """
        Add light to the module.
        :param light_to_add:
        :return:
        """
        if not isinstance(light_to_add, Light):
            raise Exception("Module light accept only Light base element")
        light_to_add.Pin = self.allocate()
        self.lights.append(light_to_add)
    
    def retrieve_light(self, light_name):
        """
        Retrieve light data from the module
        :param light_name:
        :return:
        """
        print("---")
        print(self.lights[self.lights.index(light_name)])
        return self.lights[self.lights.index(light_name)]

    def remove_light(self, light_to_remove):
        """
        Remove light from the module
        :param light_to_remove:
        :return:
        """
        if not isinstance(light_to_remove, Light):
            raise Exception("Module light accept only Light base element")
        if light_to_remove not in self.lights:
            raise Exception(f"You try to remove a {self.light_name} that is not in {self.name} lights.")
        index = self.lights.index(light_to_remove)
        self.__allocator.deallocate(index)
        self.lights.remove(light_to_remove)

    def set_light(self, light_to_set, value):
        """
        Set the value of the lamp.
        :param light_to_set:
        :param value:
        :return:
        """
        if not isinstance(light_to_set, Light):
            raise Exception(f"You can't set the value of {light_to_set}. It is not an instance of light.")

        for light in self.lights:
            if light == light_to_set:
                light.Value = value


if __name__ == "__main__":
    from package.actuator.torlight import TorLight
    import pickle
    esp = Esp32("Desktop")
    esp.append_light(TorLight())
    with open("save.json", 'wb') as file:
        pickle.dump(esp, file)

    file = open("save.json", 'rb')
    test = pickle.load(file)
    file.close()
    test.retrieve_light()

