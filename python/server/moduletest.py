from package.room.room import Room
from package.module.esp32 import Esp32

p = print

room = Room.get()
esp = Esp32("Desktop")

(room.append_module(esp))
(Room.get().append_light("Desktop", "TOR"))
(Room.get().append_light("Desktop", "MOOD"))

room.switch_on()
p(room.jsonify())
room.switch_off()
p(room.jsonify())