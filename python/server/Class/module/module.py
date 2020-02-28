from Class.allocator.pinallocator import PinAllocator

class Module:
    identifier = 0

    def __init__(self, name, start_index, end_index):
        self.allocator = PinAllocator(start_index, end_index)
        self.__name = name
        self.__identifier = 0

    def get_identifier(self):
        return self.__identifier
    
    identifier = property(get_identifier)

    def get_name(self):
        return self.__name

    name = property(get_name)

    def __str__(self):
        return self.__name
