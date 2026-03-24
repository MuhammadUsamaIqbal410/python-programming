prices = []

for i in range (8):
    price =(float(input(f"Enter price of item {i+1}: ")))
    prices.append(price)

prices.sort(reverse =True)
print (f"The sorted list of the prices is: {prices}")