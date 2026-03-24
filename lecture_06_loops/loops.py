number = [ 1,2,3,4,5,6,7,8,9,10]

for num in number:
    print(num)

fruits = ["apple", "banana", "cherry", "date", "elderberry"]
for index, fruit in enumerate(fruits):
    print(f"Index: {index}, {fruit}")

index = 0
for fruit in fruits:
    print(f"Index: {index}, {fruit}")
    index += 1

person = {
    "name": "ushna",
    "age": 25,
    "city": "lahore"}

print ("Iterating over keys:")
for key in person:
    print(f"{key}: {person[key]}")

for key, value in person.items():
    print(f"{key}: {value}")


count = 0
while count < 5:
    print(count)
    count = count +1

i = 0
for i in range(10):
    if i == 4:
        print("Skipping number 4")
        continue
    if i == 8:
        print("Breaking the loop at number 8")
        break
    print(i)
else:
    print("loop completed without a break statement")

square = [x**2 for x in range (8)]
print(square)

cubes = [ x**3 for x in range (1,11)]
for cube in cubes:
    print(cube)

name = ["ushna", "ali", "sara", "ahmed"]
age = [ 25,23,22,24]
for name, age in zip(name,age):
    print(f"{name} is {age} years old")

import itertools
colours = ["red", "green", "blue"]
count = 1
for colour in itertools.cycle(colours):
    if count > 4:
        break
    print(colour)
    count +=1
