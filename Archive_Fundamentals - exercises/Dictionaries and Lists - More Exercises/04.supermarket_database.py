storage = {}
product_info = input()
while product_info != "stocked":
    product, price, quantity = [float(x) if x[-1].isdigit() else x for x in product_info.split()]
    storage[product] = storage.get(product, {'price': price, 'quantity': 0})
    storage[product]['quantity'] += quantity
    if price != storage[product]['price']:
        storage[product]['price'] = price
    product_info = input()
total = 0
for item, info in storage.items():
    total += info['price'] * info['quantity']
    print(f"{item}: ${info['price']}0 * {int(info['quantity'])} = ${info['price'] * info['quantity']:.2f}")
print("-" * 30)
print(f"Grand Total: ${total:.2f}")
