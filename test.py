a = dict()
bureau = {
    "data": {
        "identifier": 1,
        "type": "es9"
        },
    "light":
        []
}

lit = {
    "data": {
        "identifier": 2,
        "type": "es9"
        },
    "light":
        []
}

a["bureau"] = bureau
a["lit"] = lit

for key, value in a.items():
    print(key)
    print(value)
