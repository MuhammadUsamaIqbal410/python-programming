# applying map function for temperature conversion

temp = [34,23,53,55,32,51,43]
def to_fahrenhiet(c):
    return (c * 9/5)+32
fahrenhiet = list(map(to_fahrenhiet, temp))
print(fahrenhiet)

# OR 

fahrenhiet = list(map(lambda c : (c * 9/5) + 32, temp))
print(fahrenhiet)

