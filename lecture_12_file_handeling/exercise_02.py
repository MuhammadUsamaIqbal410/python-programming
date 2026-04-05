
# problem no 02: taking the input from the user and 
# printing the content if exist otherwise raise error

a = input ("Enter the name of the file: ").lower()

try: 
    with open(a, "r")as file:
        content = file.read()
        print(content)
except FileNotFoundError:
    print("File does not exist")