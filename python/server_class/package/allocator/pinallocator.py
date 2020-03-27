import pickle
class PinAllocator:

    def __init__(self, start_index, end_index):
        self.available_pin_list = [i for i in range(start_index, end_index)]
        self.used_pin_list = []

    def allocate(self):
        try:
            pin_to_allocate = self.available_pin_list.pop(0)
            self.used_pin_list.append(pin_to_allocate)
            return pin_to_allocate
        except IndexError:
            return -1

    def deallocate(self, pin_to_deallocate):
        try:
            self.used_pin_list.remove(pin_to_deallocate)
            self.available_pin_list.append(pin_to_deallocate)
        except ValueError:
            pass


if __name__ == "__main__":

    fdp = PinAllocator(0, 25)
    print(fdp)
    filefdp = open('save.json', 'wb')
    pickle.dump(fdp, filefdp)
    filefdp.close()