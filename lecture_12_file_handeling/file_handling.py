
# opening a file eith write mode

first = open("new_file.txt", "w")
first.write("I have created a python file and practising the work on it")
first.close()

#writing and reading a file using exception handling with try except method

try:
    with open("new_file.txt", "r") as file:
        content = file.read()
        print("file content =", content)
except FileNotFoundError:
    print("Error: File you are searching for does not exist.")

# writing a file using with statment and write mode

with open("new_file1.txt", "w") as file:
    file.write("Practising the file handling as the practise make the man perfect")
print("File written Successfully")

# Appending to a file using with statement and append mode

with open("new_file1.txt","a") as file:
    file.write("\n I am writing while using the append mode and it will not overwrite the existing content")
print("File written successfully")

# Appending to a file using with statement and read and write mode

with open ("new_file.txt","r+") as file:
    content = file.read()
    print("file content =", content)
    file.write("\n I am writing while using the read and write mode and it will not overwrite the" \
    " existing content")
print("File written successfully")

#Reading and writing a file using with statement and read mode

with open("new_file.txt","r") as file:
    content = file.read()
    print("file content = ", content)

with open("new_file.txt", "w") as file:
    file.write("I am writing while using the write mode" \
    "and it will overwrite the existing content")
    print("File written successfully")


#working with json file in python
import json

data = {
    "name": "Usama",
    "age": 25,
    "city": "Lahore"

}

with open("data.json","w") as file:
    json.dump(data,file)

with open("data.json", "r") as file:
    data = json.load(file)
    print("data from json file = ", data)


#Handling file extensions in python
import os
try:
    with open("non_existant_file.txt", "r") as file:
        content = file.read()
        print("File content = ", content)

except FileNotFoundError:
    print("Error: File not found.")

