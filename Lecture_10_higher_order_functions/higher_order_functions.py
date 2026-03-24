# applying map function

def double(x):
    return x*2
numbers = [1,2,3,4,5,6,7]
doubled = list(map(double, numbers))
print(doubled)

# OR in the same way 

doubled = list(map(lambda x: x*2, numbers))
print(doubled)


# Applying fitler function

def is_even(x):
    return x%2 == 0
evens = list(filter(is_even, numbers))
print(evens)

# In the same way

evens = list(filter(lambda x : x%2 ==0, numbers))
print(evens)

# Applying reduce function 

from functools import reduce
def multiply(x,y):
    return x*y
product = reduce(multiply, numbers)
print(product)

# Similarly

product = reduce(lambda x,y : x*y , numbers)
print(product)

# Applying enumerate to the function

fruits = ["apple", "banana", "cherry",]
for index, fruit in enumerate(fruits, start = 1):
    print(f"{index}: {fruit}")

