from package.room.room import Room
from package.module.esp32 import Esp32
p = print

room = Room.get()
esp = Esp32("Desktop")
# esp2 = Esp32("Bed")


p(room.append_module(esp))
# p(room.append_module(esp2))
print("Adding light")
p(Room.get().append_light("Desktop", "TOR"))
p(Room.get().append_light("Desktop", "MOOD"))
p(Room.get().append_light("Desktop", "RGB", "bureau"))

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

print(f"\n{room}")
print(f"{room2}")
