import json

fav_num = input("What is your favorite number?: ")
filename = "fav_num.json"

with open(filename, 'w') as f:
    json.dump(fav_num, f)