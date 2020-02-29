from Class.allocator.idallocator import IdAllocator


class Room():

    def __init__(self):
        self.__id_allocator = IdAllocator()
        self.__module = []

    def append_module(self, module):
        self.__module.append(module)

if __name__=="__main__":
    a = Room