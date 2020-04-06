import json


class Utils:

    @staticmethod
    def save_data(data_to_save):
        with open("old_data.json", "w") as file:
            json.dump(data_to_save, file, indent=4)

    @staticmethod
    def get_data():
        with open("old_data.json", "r") as file:
            return json.load(file)

    @staticmethod
    def get_switch_on_value():
        # todo
        return 200

    @staticmethod
    def save_module(module_type, module):
        data = Utils.get_data()
        data[module.name] = {
                "data": {
                    "identifier": module.identifier,
                    "type": module_type
                },
                "light":
                {}
            }
        Utils.save_data(data)

    @staticmethod
    def delete_module(module_name):
        data = Utils.get_data()
        del data[module_name]
        print(data)
        Utils.save_data(data)

    @staticmethod
    def save_light(module, light):
        data = Utils.get_data()
        data[module]["light"][light.name] = {
            "pin": light.pin,
            "value": light.value,
            "type": light.get_type()
        }
        Utils.save_data(data)

    @staticmethod
    def delete_light(module_name, light_name):
        data = Utils.get_data()
        del data[module_name]["light"][light_name]
        Utils.save_data(data)


if __name__ == "__main__":
    a = Utils.get_data()
    Utils.save_data({"a": "coucou"})
