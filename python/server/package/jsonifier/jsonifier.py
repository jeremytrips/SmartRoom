from package.singelton.singelton import Singleton

"""
Will be used to select the data needed in while jsonify
"""


class Jsonifier:

    def __init__(self):
        self.__data_layout = None
        self._reset()

    def success(self, data):
        self.__data_layout["success"].append(data)

    def data(self, data):
        self.__data_layout["data"].append(data)

    def error(self, data):
        self.__data_layout["error"].append(data)

    def _reset(self):
        self.__data_layout = {
            "success": [],
            "data": [],
            "error": []
        }

    def get(self):
        temp = dict()
        for entry in self.__data_layout:
            if len(self.__data_layout[entry]) != 0:
                temp[entry] = self.__data_layout[entry]
        self._reset()
        return temp

    def __iadd__(self, other):
        for key, values in other.items():
            for value in values:
                self.__data_layout[key].append(value)
        return self

    def describe(self):
        print({
            "success": self.__data_layout["success"],
            "Len success": len(self.__data_layout["success"]),
            "data": str(self.__data_layout["data"]),
            "Len data": len(self.__data_layout["data"]),
            "error": self.__data_layout["error"],
            "Len error": len(self.__data_layout["error"]),
        })


if __name__ == "__main__":
    a = Jsonifier()
    a.data({'name': 'Mood light 1', 'value': 0})
    a.data({'name': 'Mabite', 'value': 0})
    a.error("NOT_EXIST")
    b = Jsonifier()
    b.data({'name': 'Tor light 2', 'value': 1})
    b.success("LIGHT_ADDED")
    a += b.get()
    print(a.describe())
    print(a.get())
