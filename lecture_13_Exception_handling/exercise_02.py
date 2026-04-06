
try:
    name = str(input("Enter your name: "))
    a = int(name)

except ValueError:
    print("Invalid input. Please enter a valid name.")
except Exception as e:
    print("An error occurred:", e)