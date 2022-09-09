storage = dict()

products = input()
while products != "buy":
    products = products.split()

    product_name, product_price, product_quantity = [float(item) if item[-1].isdigit() else item for item in products]
    storage[product_name] = storage.get(product_name, {"price": product_price, "quantity": product_quantity})

    if storage[product_name]["price"] != product_price:
        storage[product_name]["price"] = product_price
        storage[product_name]["quantity"] += product_quantity
    products = input()

for key, values in storage.items():
    print(f"{key} -> {storage[key]['quantity'] * storage[key]['price']:.2f} ")


# orders = dict()
#
#
# products = input()
# while products != "buy":
#     products = products.split()
#
#     product = products[0]
#     price = float(products[1])
#     quantity = int(products[2])
#
#     if product not in orders:
#         orders[product] = [price, quantity]
#
#     elif product in orders:
#         orders[product][1] += quantity
#         if price != orders[product][0]:
#             orders[product][0] = price
#
#     products = input()
#
# for product in orders:
#     total_price = orders[product][0] * orders[product][1]
#     print(f"{product} -> {total_price:.2f}")
