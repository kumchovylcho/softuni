products_with_quantities = input().split()
wanted_products = input().split()

products = {}

for product in range(0, len(products_with_quantities), 2):
    key = products_with_quantities[product]
    value = products_with_quantities[product + 1]
    products[key] = int(value)

for product in wanted_products:
    if product in products:
        print(f"We have {products[product]} of {product} left")
    elif product not in products:
        print(f"Sorry, we don't have {product}")

print(len(products))