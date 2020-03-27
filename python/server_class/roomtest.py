from package.room.room import Room
from package.actuator.moodlight import MoodLight
from package.actuator.torlight import TorLight
from package.actuator.rgblight import RgbLight
from package.module.esp32 import Esp32

import pickle
import json

import settings

room = Room()
esp = Esp32("Desktop")

room.append_module(esp)
room.append_light(esp, "TOR")
#room.retrieve_light("Desktop", "Tor light 1")

file = open("save.json", 'rb')
pickle.load(file)
file.close()

#retrieve_light("Desktop", "Tor light 1")
