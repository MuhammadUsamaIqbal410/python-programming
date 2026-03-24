# Numbering the shopping items using the enumerate function

shopping_list = ["face wash", "mounth wash", "cleansing cream", "hair shinner"]

for index, shopping in enumerate(shopping_list, start= 1):
    print(f"{index}: {shopping}")