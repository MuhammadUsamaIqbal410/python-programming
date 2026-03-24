import random
def apply_discount(original_price, discount_percentage):

    final_price = original_price -(original_price * discount_percentage / 100)
    return final_price

price = random.randint(1,1000)
discount = random.randint(1,50)
final_price = apply_discount(price,discount)

print(f"Original price: ${price}")
print(f"Discount percentage: {discount}%")
print(f"Final price after discount: ${final_price:.2f}")