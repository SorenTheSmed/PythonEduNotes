import json

data = {"name": "Daniel", "age": "36"}

with open("data.txt", "w") as outfile:
    json.dump(data, outfile)