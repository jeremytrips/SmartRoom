

class PinAllocator():

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

    def unallocate(self, pin_to_unallocate):
        try:
            self.used_pin_list.remove(pin_to_unallocate)
            self.available_pin_list.append(pin_to_unallocate)
        except ValueError:
            pass