def shopping_cart(*args):
    meals_limit = {
        'Soup': 3,
        'Pizza': 4,
        'Dessert': 2
    }
    products = {
        'Soup': set(),
        'Pizza': set(),
        'Dessert': set()
    }
    is_empty = True
    for command in args:
        if command == "Stop":
            break
        meal, product = command
        if len(products[meal]) < meals_limit[meal]:
            products[meal].add(product)
            is_empty = False
    output = ""
    for key, value in sorted(products.items(), key=lambda x: (-len(x[1]), x[0])):
        output += f"{key}:\n"
        for item in sorted(value):
            output += f" - {item}\n"
    if is_empty:
        return "No products in the cart!"
    return output
