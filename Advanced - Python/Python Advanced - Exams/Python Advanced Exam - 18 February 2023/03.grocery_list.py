def shop_from_grocery_list(budget: int, grocery_list: list, *args):
    for item, price in args:
        if item in grocery_list and budget >= price:
            budget -= price
            grocery_list.remove(item)

        elif budget < price:
            break

    if not grocery_list:
        return f"Shopping is successful. Remaining budget: {budget:.2f}."
    return f"You did not buy all the products. Missing products: {', '.join(grocery_list)}."


print(shop_from_grocery_list(
    100,
    ["tomato", "cola"],
    ("cola", 5.8),
    ("tomato", 10.0),
    ("tomato", 20.45),
))


print(shop_from_grocery_list(
    100,
    ["tomato", "cola", "chips", "meat"],
    ("cola", 5.8),
    ("tomato", 10.0),
    ("meat", 22),
))


print(shop_from_grocery_list(
    100,
    ["tomato", "cola", "chips", "meat", "chocolate"],
    ("cola", 15.8),
    ("chocolate", 30),
    ("tomato", 15.85),
    ("chips", 50),
    ("meat", 22.99),
))