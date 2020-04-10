import package.jsonifier.jsonifier as jf


class PinAllocator:

    def __init__(self, start_index, end_index):
        self.available_pin_list = [i for i in range(start_index, end_index)]
        self.used_pin_list = []
        self.__jsonifier = jf.Jsonifier()

    def jsonify(self):
        jsonifier = jf.Jsonifier()
        jsonifier.data({
            "type": "pin_allocator",
            "available_pin": self.available_pin_list,
            "used_pin": self.used_pin_list
        })
        return jsonifier.get()

    def set_used(self, used_pin):
        self.available_pin_list.remove(used_pin)
        self.used_pin_list.append(used_pin)

    def allocate(self):
        try:
            pin_to_allocate = self.available_pin_list.pop(0)
            self.used_pin_list.append(pin_to_allocate)
            self.__jsonifier.success("PIN_ALLOCATE")
            self.__jsonifier.data({"pin": pin_to_allocate})
            return self.get()
        except IndexError:
            self.__jsonifier.error("NO_MORE_PIN")
            return self.get()

    def deallocate(self, pin_to_deallocate):
        try:
            self.used_pin_list.remove(pin_to_deallocate)
            self.available_pin_list.append(pin_to_deallocate)
            self.__jsonifier.success("PIN_DEALLOCATE")
            return self.get()
        except ValueError:
            self.__jsonifier.error("PIN_NOT_ALLOCATE")
            return self.get()

    def get(self):
        return self.__jsonifier.get()


if __name__ == "__main__":

    fdp = PinAllocator(0, 25)
    print(fdp)
    filefdp = open('save.json', 'wb')
    pickle.dump(fdp, filefdp)
    filefdp.close()