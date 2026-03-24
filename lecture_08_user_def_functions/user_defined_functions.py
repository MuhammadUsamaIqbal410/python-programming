def add(num1, num2, num3):
    print("Number 1: ", num1)
    print("Number 2: ", num2)
    print("Number 3: ", num3)
    
    addition = num1 + num2 + num3
    count = 3
    modulus = addition % count
    return addition,count, modulus
result = add(10, 20, 30)
print("The addition for the three numbers is: ", result)
print("the modulus of the numbers is: ", result[2])

def greet():
    print("Hello, Welcome to the world of python programming!")
greet()

def name(fname, mname = "Usama", lname = "Iqbal"):
    print("Hello", fname, mname, lname)
name("Muhammad")
name("Muhammad", "Usama")
name("Muhammad", "Usama", "Iqbal")
name("Muhammad", )

def name(*names):
    print("Hello",names[0], names[1], names[2],)
name ("Muhammad", "Ali", "ul Murataza")

def name(fname, mname, lname):
    return "Hello, " + fname + " " + mname + " " + lname 
result = name("Muhammad", "Umar", "Farooq")
print(result)

