print("Welcome to the Python Functions")

prices= [100, 200, 300, 400, 500]
highest_price = max(prices)
# length = len(highest_price)
print(highest_price)

ratings = [4.5, 3.8, 4.2, 5.0, 4.0]
sorted = sorted (ratings)
print(sorted)

for i in range(5):
    print("Dish", i+1, "is good to live")

expression = "5 + 3*2"
result = eval(expression)
print(result)