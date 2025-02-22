
from package.actuator.moodlight import MoodLight
from package.actuator.torlight import TorLight
from package.actuator.rgblight import RgbLight
from package.module.esp32 import Esp32


IP_ADDRESS = "localhost"
IP_PORT = -1

PORT_NUMBER = 8585

LIGHT_TYPE = {"RGB": RgbLight, "TOR": TorLight, "MOOD": MoodLight}
MODULE_TYPE = {"esp32": Esp32}

SWITCH_ON_VALUE = 200

debug = True
