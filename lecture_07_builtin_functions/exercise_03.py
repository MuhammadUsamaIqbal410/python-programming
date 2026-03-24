number = []

for i in range(5):
    num = int(input(f"Enter a number {i+1}: "))
    number.append(num)
print("The list of my numbers is :", number)

sort = sorted(number)
print("The sorted list of my numbers is: ", sort)
maximum = max(number)
print(f"The maximum number in the list is: {maximum} " )


