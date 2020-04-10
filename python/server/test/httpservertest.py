import requests
import package.room.room as room
import time
rg = requests.get
room = room.Room.get()
print(f"http server test: {id(room)}")
print(rg("http://localhost:5050/module/add/esp32/test").content)

"""
print(rg("http://localhost:5050/module/add/esp32/").content)

print(rg("http://localhost:5050/module/retrieve/test").content)

print(rg("http://localhost:5050/module/add/Esp32/test").content)

print(rg("http://localhost:5050/light/add/test/TOR").content)

print(rg("http://localhost:5050/light/add/test/RGB").content)
print(rg("http://localhost:5050/light/add/test/RGB").content)
print(rg("http://localhost:5050/light/add/test/RGB").content)
print(rg("http://localhost:5050/light/add/test/RGB").content)
print(rg("http://localhost:5050/light/add/test/RGB").content)
print(rg("http://localhost:5050/light/add/test/RGB").content)
print(rg("http://localhost:5050/light/add/test/RGB").content)
print(rg("http://localhost:5050/light/add/test/RGB").content)
print(rg("http://localhost:5050/light/add/test/RGB").content)
print(rg("http://localhost:5050/light/add/test/RGB").content)
print(rg("http://localhost:5050/light/add/test/RGB").content)
print(rg("http://localhost:5050/light/add/test/RGB").content)
print(rg("http://localhost:5050/light/add/test/RGB").content)
print(rg("http://localhost:5050/light/add/test/RGB").content)

print(rg("http://localhost:5050/light/add/test/MOOD").content)

print(rg("http://localhost:5050/module/retrieve/test").content)
"""