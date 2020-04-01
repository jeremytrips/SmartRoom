from package.room.room import Room
from package.module.esp32 import Esp32
p = print

room = Room.get()

print("Adding module")
p(room.append_module("esp32", "Desktop"))
p(room.append_module("esp32", "Desktop"))
p(room.append_module("esp32"))
p(room.append_module("esp32"))
p(room.append_module("esp32"))
p(room.append_module("esp32"))
p(room.append_module("esp32"))
p(room.append_module("esp32"))
p(room.append_module("esp32"))
p(room.append_module("esp32"))
p(room.append_module("esp32"))

print("To much id")
p(room.append_module("esp32", "test"))

print("Retrieving module")
p(room.retrieve_module("Desktop"))

print("Removing module")
p(room.remove_module("test"))

print("Adding light")
p(Room.get().append_light("Desktop", "TOR"))
p(Room.get().append_light("Desktop", "MOOD"))
p(Room.get().append_light("Desktop", "RGB", "bureau"))
p(Room.get().append_light("Desktop", "RGB", "bureau"))
p(Room.get().append_light("Desktop", "RGccB", "bureau"))

print("Adding light in Module 1")
p(Room.get().append_light("Module 1", "RGB", "bureau"))
p(Room.get().append_light("Module 1", "RGccB", "bureau"))
p(Room.get().append_light("Module 1", "RGB"))
p(Room.get().append_light("Module 1", "TOR"))


print("Setting light")
p(Room.get().set_light("Desktop", "bureau", [-31, -36, 13525]))
p(Room.get().set_light("Desktop", "bureau", [256, -36, 125]))
p(Room.get().set_light("Desktop", "bureau", [125, 26, 25]))

p(Room.get().set_light("Desktop", "Mood light 1", 126))
p(Room.get().set_light("Desktop", "Mood light 1", 3641))
p(Room.get().set_light("Desktop", "Mood light 1", -25))

p(Room.get().set_light("Desktop", "Tor light 1", 1))
p(Room.get().set_light("Desktop", "Tor light 1", 0))
p(Room.get().set_light("Desktop", "Tor light 1", 1))

print("Retrieving light")
p(Room.get().retrieve_light("Desktop"))
p(Room.get().retrieve_light("Desktop", "Mood light 1"))
p(Room.get().retrieve_light("Desktop", "Tor light "))

room2 = Room.get()
print("Switching off")
p(room2.switch_off())

print("Switching on")
p(room2.switch_on())

print("Retrieving lights")
print(room2.retrieve_light("Desktop"))
print(room2.retrieve_light("Bed"))

print("Retrieving room")
p(room.jsonify())

