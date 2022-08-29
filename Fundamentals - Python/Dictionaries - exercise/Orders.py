orders = dict()


products = input()
while products != "buy":
    products = products.split()

    product = products[0]
    price = float(products[1])
    quantity = int(products[2])

    if product not in orders:
        orders[product] = [price, quantity]

    elif product in orders:
        orders[product][1] += quantity
        if price != orders[product][0]:
            orders[product][0] = price

    products = input()

for product in orders:
    total_price = orders[product][0] * orders[product][1]
    print(f"{product} -> {total_price:.2f}")
