
attempts = 5

while attempts > 0:
    try:
        n = int(input("Enter the number of elements you want to add in the list : "))
        if n < 0 or n > 20:
            print("Please enter a number between 0 and 20")
        else:   
            break
    except ValueError:
        print("Please enter a valid integer")
    attempts -= 1

if attempts == 0:
    print("Maximum attempts reached. Exiting.")
    exit()

l = []
for i in range(n):
    element = input(f"Enter the element no {i+1} for the list: ")
    l.append(element)
    print(f"The list is : {l}")


attempts = 5

while attempts > 0:
    attempts -= 1
    try:
        index = int(input("Enter the index you want to retrieve: "))
        if index < 0 or index >= n:
            print("Please enter a valid index")
        else:
            print(f"Element at index {index} is : {l[index]}")
            break
    except IndexError as e:
        print(f"Please enter a valid index: {e}")
    except ValueError:
        print("Please enter a valid integer")