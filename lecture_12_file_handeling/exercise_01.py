# wrinting  a python program that reads and prints the lines of the file

#opening the file using json

import json

data = {"name": "Usama", "age": 25, "city": "Lahore"}
with open("data.json", "w") as file:
    json.dump(data, file, indent=4)

with open("data.json", "r") as file:
    lines = file.readlines()
    print("Total lines = ", len(lines))
    # for line in lines:
    #     print(line.strip())
