import json

data = {
    "name": "Avishek",
    "age": 22,
    "isStudent": True
}

with open("FileHandling/data.json", "w") as f:
    json.dump(data, f, indent=2)