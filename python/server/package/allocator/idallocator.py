

class IdAllocator():

    def __init__(self):
        self.available_id_list = [i for i in range(10)]
        self.used_id_list = []

    def allocate(self):
        try:
            id_to_allocate = self.available_id_list.pop(0)
            self.used_id_list.append(id_to_allocate)
            return id_to_allocate
        except IndexError:
            return -1

    def unallocate(self, id_to_unallocate):
        try:
            self.used_id_list.remove(id_to_unallocate)
            self.available_id_list.append(id_to_unallocate)
        except ValueError:
            pass