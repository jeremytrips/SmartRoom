from package.actuator.moodlight import MoodLight
from package.actuator.torlight import TorLight
from package.actuator.rgblight import RgbLight

IP_ADDRESS = "localhost"
IP_PORT = -1

PORT_NUMBER = 8585

LIGHT_TYPE = {"RGB": RgbLight, "TOR": TorLight, "MOOD": MoodLight}