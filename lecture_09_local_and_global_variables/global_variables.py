x = 3
def my_function():
    y = 5
    print(f"inside function: x = {x}, y = {y}")
my_function()
print(f"outside function: x = {x}")
# print(f"outside finction: x = {y}")   cannot be called outside the function


x = "global"
def outer_function():
    x = "enclosing"
    def inner_function():
        x = "local"
        print("inside function: ", x)
    inner_function()
    print("outer_function: ", x)
outer_function()
print("Outside all function: ", x)



counter = 0 
def increment():
    global counter
    counter +=1
increment()
print("Updated counter: ", counter)



a = [1,2,3]
b = a
c = [1,2,3]
print(id(a), id(b), id(c))
print(a is b)
print(a is c)
print(a == c)