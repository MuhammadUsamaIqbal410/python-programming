# Problem No 03: Exception handling for the age
while True:

    try: 
        age = int (input("Enter your age: "))
    except ValueError:
        print("Invalid input. Please enter a valid age.")
        continue

    if age <= 0 or age > 110:
        print("Age must be between 1 and 110")
        continue
    elif age < 18:
        print("You are very young.")
    elif age >= 18 and age < 40:
        print("You are in the age of adulthood.")
    elif age >= 40 and age < 60:
        print("You are middle aged person.")
    else:
        print("You are a senior citizen now. Go find a better and more fulfilling life.")
    break