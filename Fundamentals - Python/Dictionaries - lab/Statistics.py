products_in_stock = dict()

fill_in_products = input()
while fill_in_products != "statistics":
    fill_in_products = fill_in_products.split(": ")
    product = fill_in_products[0]
    quantity = int(fill_in_products[1])

    if product not in products_in_stock:
        products_in_stock[product] = quantity

    elif product in products_in_stock:
        products_in_stock[product] += quantity

    fill_in_products = input()

print("Products in stock:")

for item in products_in_stock:
    print(f"- {item}: {products_in_stock[item]}")

print(f"Total Products: {len(products_in_stock)}")
print(f"Total Quantity: {sum(products_in_stock.values())}")