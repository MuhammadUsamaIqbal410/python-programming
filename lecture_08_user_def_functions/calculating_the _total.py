import random
def calculate_total(price_per_item, quantity):
    total = price_per_item * quantity
    return total
price = random.randint(1,10)
quantity = random.randint(1,10)


result = calculate_total(price,quantity)

print(f"price per item: {price}")
print(f"Quantity: {quantity}")
print(f"Total price for the item is: {result}")