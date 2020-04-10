import json


class Utils:

    @staticmethod
    def save_data(data_to_save):
        pass

    @staticmethod
    def get_data():
        pass

    @staticmethod
    def get_switch_on_value():
        # todo
        return 200

    @staticmethod
    def save_module(module_type, module):
        data = Utils.load_backup()
        data[module.name] = {
                "data": {
                    "identifier": module.identifier,
                    "name": module.name,
                    "type": module_type
                },
                "light":
                {}
            }
        Utils.save_backup(data)

    @staticmethod
    def delete_module(module_name):
        data = Utils.load_backup()
        del data[module_name]
        print(data)
        Utils.save_backup(data)

    @staticmethod
    def save_light(module, light):
        data = Utils.load_backup()
        data[module]["light"][light.name] = {
            "pin": light.pin,
            "value": light.value,
            "type": light.get_type()
        }
        Utils.save_backup(data)

    @staticmethod
    def delete_light(module_name, light_name):
        data = Utils.load_backup()
        del data[module_name]["light"][light_name]
        Utils.save_backup(data)

    @staticmethod
    def load_backup():
        with open("backup.json", "r") as file:
            return json.load(file)

    @staticmethod
    def save_backup(data):
        with open("backup.json", "w") as file:
            json.dump(data, file, indent=3)


if __name__ == "__main__":
    pass
