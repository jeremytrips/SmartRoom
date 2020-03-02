from package.allocator.pinallocator import PinAllocator

class Module:

    def __init__(self, name, identitfier, start_index, end_index):
        self.__allocator = PinAllocator(start_index, end_index)
        self.name = name
        self.identifier = identitfier
        client = 

    def send(self, data):
        self.

    def allocate(self):
        return self.__allocator.allocate()

    def get_identifier(self):
        return self.identifier
    
    identifier = property(get_identifier)

    def get_name(self):
        return self.name

    name = property(get_name)

    def __str__(self):
        return self.name
