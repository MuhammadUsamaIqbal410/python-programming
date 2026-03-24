try:
    a = int(input("Enter the amount you wanna withdraw: "))
    
    amount = 19900

    if a > amount:
        print("Insufficient balance")

    elif a< amount:
        print("please wait for a while, your transaction is being processed")
    
    else: 
        print("please enter the number in multiples of 500")

except ValueError:
    print("Invalid input. Please enter a valid number.")
    