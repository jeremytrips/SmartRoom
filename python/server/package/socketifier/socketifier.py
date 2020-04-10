import package.enums.mapper as mapper
"""
data frame:
    byte | data
      0  | number of pin sended
      1  | pin number
      2  | value to write
      3  |
"""


class Socketifier:

    def __init__(self):
        self.__data_to_write = list()

    def set_data(self, light):
        pass

    @staticmethod
    def Socketify(action, data):
        """
        [{'test': [{'name': 'r', 'value': [125, 125, 125], 'pin': 16}]}]
        :param data:
        :return:
        """
        formatted_data = list()
        for module in data:
            # module is a dict whit module name as key and list of jsonify data list as value
            for module_name in module.keys():
                print(module)
                for light in module[module_name]:
                    if isinstance(light["value"], list):
                        # Multiple pin light
                        # just set the data multiple times in the formatted data list
                        # todo
                        pass
                    else:
                        # Single pin light
                        # todo
                        pass