products_statistics = {}
products = input()
while products != "statistics":
    products = products.split(": ")
    key = products[0]
    value = int(products[1])
    if key not in products_statistics:
        products_statistics[key] = 0
    products_statistics[key] += value
    products = input()

print("Products in stock:")

for (product, quantity) in products_statistics.items():
    print(f"- {product}: {quantity}")

print(f"Total Products: {len(products_statistics)}")
print(f"Total Quantity: {sum(products_statistics.values())}")