from package.room.room import Room
from package.module.esp32 import Esp32


room = Room.get()
esp = Esp32("Desktop")

room.append_module(esp)
room.append_light("Desktop", "TOR")
room.append_light("Desktop", "MOOD")
room.append_light("Desktop", "RGB", "bureau")

room.set_light("Desktop", "bureau", [-31, -36, 13525])
room.set_light("Desktop", "bureau", [256, -36, 125])
room.set_light("Desktop", "bureau", [125, 26, 25])

room.set_light("Desktop", "Mood light 1", 126)
room.set_light("Desktop", "Mood light 1", 3641)
room.set_light("Desktop", "Mood light 1", -25)

room.set_light("Desktop", "Tor light 1", 1)
room.set_light("Desktop", "Tor light 1", 0)
room.set_light("Desktop", "Tor light 1", 1)

room.retrieve_light("Desktop", "bureau")
room.retrieve_light("Desktop", "Mood light 1")
room.retrieve_light("Desktop", "Tor light 1")

room2 = Room.get()
print("\nSwitching off")
room2.switch_off()
room2.retrieve_light("Desktop", "bureau")
room2.retrieve_light("Desktop", "Mood light 1")
room2.retrieve_light("Desktop", "Tor light 1")

print("\nSwitching on")
room2.switch_on()
room2.retrieve_light("Desktop", "bureau")
room2.retrieve_light("Desktop", "Mood light 1")
room2.retrieve_light("Desktop", "Tor light 1")

print(f"\n{room}")
print(f"{room2}")