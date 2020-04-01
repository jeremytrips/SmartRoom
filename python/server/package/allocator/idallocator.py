from package.jsonifier.jsonifier import Jsonifier
"""
    TODO: eventually a parent class Allocator

"""


class IdAllocator:

    def __init__(self):
        self.available_id_list = [i for i in range(10)]
        self.used_id_list = []
        self.__jsonifier = Jsonifier()

    def jsonify(self):
        jsonifier = Jsonifier()
        jsonifier.data({
            "type": "id_allocator",
            "available_id": self.available_id_list,
            "used_id": self.used_id_list
        })
        return jsonifier.get()

    def allocate(self):
        try:
            id_to_allocate = self.available_id_list.pop(0)
            self.used_id_list.append(id_to_allocate)
            self.__jsonifier.success("ID_ALLOCATE")
            return id_to_allocate
        except IndexError:
            self.__jsonifier.error("NO_MORE_ID")
            return self.get()

    def deallocate(self, id_to_deallocate):
        try:
            self.used_id_list.remove(id_to_deallocate)
            self.available_id_list.append(id_to_deallocate)
            self.__jsonifier.success("ID_DEALLOCATE")
            return self.get()
        except ValueError:
            self.__jsonifier.error("ID_NOT_ALLOCATE")
            return self.get()

    def get(self):
        return self.__jsonifier.get()
