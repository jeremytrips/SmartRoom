class Module:

    def __init__(self, name):
        self._name = name

    def name(self):
        return self._name

    name = property(name)

    def __str__(self):
        return self._name
