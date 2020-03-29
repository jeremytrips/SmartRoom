from package.singelton.singelton import Singleton

# TODO:

"""
Will be used to select the data needed in while jsonify
"""


class Jsonifier:

    def __init__(self):
        self.data_layout = None
        self._reset()

    def success(self, data):
        self.data_layout.update(data)

    def data(self, data):
        self.data_layout["data"].update(data)

    def error(self, data):
        self.data_layout["error"].append(data)

    def multiple_data(self, success=None, data=None, error=None):
        self.data_layout.update(success)
        self.data_layout["data"].append(data)
        self.data_layout.update(error)

    def _reset(self):
        self.data_layout = {
            "success": [],
            "data": {},
            "error": []
        }

    def get(self):
        temp = dict()
        for entry in self.data_layout:
            if len(self.data_layout[entry]) != 0:
                temp[entry] = self.data_layout[entry]
        self._reset()
        return temp


if __name__ == "__main__":
    pass
