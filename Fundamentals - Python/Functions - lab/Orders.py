product = input()
quantity = int(input())
price = 0


def prices(type_of_product, number_of_products, cash):
    if type_of_product == "coffee":
        cash = 1.50
    elif type_of_product == "water":
        cash = 1.00
    elif type_of_product == "coke":
        cash = 1.40
    elif type_of_product == "snacks":
        cash = 2.00
    result = cash * number_of_products
    return f"{result:.2f}"


print(prices(product, quantity, price))
