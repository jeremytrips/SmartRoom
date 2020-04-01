import unittest
from package.room.room import Room

# todo


class MyTestCase(unittest.TestCase):
    def test_something(self):
        room = Room.get()
        # Adding module test
        self.assertEqual(room.append_module("esp32", "Desktop"), {'success': ['MODULE_ADDED']})
        self.assertEqual(room.append_module("esp32", "Desktop"), {'error': ['MODULE_ALREADY_EXIST_ERROR']})
        self.assertEqual(room.append_module("esp32"), {'success': ['MODULE_ADDED']})
        self.assertEqual(room.append_module("esp32", "test"), {'success': ['MODULE_ADDED']})

        # Removing module
        self.assertEqual(room.remove_module("test"), {'success': ['MODULE_ADDED']})


if __name__ == '__main__':
    unittest.main()
