
# Exception handling for the zeor division error

try: 
    num = int(input("Enter the number: "))
    div = round(10 / num, 4)
    print(f"Result : {div: .4f}")
    
except ZeroDivisionError:
    print("Error: Division by zero is not allowed.")

# Exception handling for the multiple errors like value error and zero division error

try: 
    numinator = int(input("Enter the first number: "))
    demoninator = int(input("Enter the second number: "))
    div = round(numinator / demoninator, 4)
    print(f"Result : {div: .4f}")

except ZeroDivisionError:
    print("Error: You cannot divide by zero.")
except ValueError:
    print("Error: Invalid Input. Please enter a valid integer.")


# Catching any exception

try:
    numinator = int(input("Enter the first number: "))
    demoninator = int(input("Enter the second number: "))
    div = round(numinator / demoninator, 4)
    print(f"Result : {div: .4f}")

except Exception as e:
    print(f"An error occurred: {e}")


# Using finally block

try:
    file = open("new_file.txt", "r")
    content = file.read()

except FileNotFoundError:
    print("File does not exist!")
finally:
    print("Closing the file...")
    file.close()
    print("File closed successfully!")


# Case scenario for the exception handling

def withdraw(amount, balance):

    try:
        if amount > balance:
            raise ValueError("Insufficient funds.")
        balance -= amount
        print(f"withdrawal successful! Remaining balance: {balance}")
    except ValueError as e:
        print(f"Error: {e}")

try:
    withdraw(1500, 1000)
except ValueError as e:
    print(f"Error: {e}")


