import json

with open("FileHandling/data.json", "r") as f:
    py_obj = json.load(f)
    print(py_obj, type(py_obj))