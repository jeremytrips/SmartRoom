import json


class Utils:

    @staticmethod
    def save_data(data_to_save):
        data = Utils.get_data()
        data.update(data_to_save)
        with open("old_data.json", "w") as file:
            json.dump(data, file, indent=4)

    @staticmethod
    def get_data():
        with open("old_data.json", "r") as file:
            return json.load(file)

    @staticmethod
    def get_switch_on_value():
        # todo
        return 200


if __name__ == "__main__":
    a = Utils.get_data()
    Utils.save_data({"a": "coucou"})
