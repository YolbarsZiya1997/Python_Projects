import json

filename = "fav_num.json"
with open(filename) as f:
    fav_num = json.load(f)
    print(f"I know your favorite number, it is {fav_num}")