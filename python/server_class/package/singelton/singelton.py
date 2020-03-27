
class Singleton:

    def __init__(self, decorated):
        self._decorated = decorated
        self._instance = None

    def get(self):
        try:
            return self._instance
        except AttributeError:
            self._instance = self._decorated()
            return self._instance

    def __call__(self):
        raise TypeError('Singletons must be accessed through `Instance()`.')
