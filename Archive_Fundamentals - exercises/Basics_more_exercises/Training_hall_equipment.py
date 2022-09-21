budget, items_to_buy = int(input()), int(input())
money_spent = 0

for count in range(items_to_buy):
    item_name, item_price, item_count = input(), float(input()), int(input())
    if item_count > 1:
        item_name += "s"
    print(f"Adding {item_count} {item_name} to cart.")
    money_spent += item_price * item_count
print(f"Subtotal: ${money_spent:.2f}")
if money_spent <= budget:
    print(f"Money left: ${budget - money_spent:.2f}")
else:
    print(f"Not enough. We need ${money_spent - budget:.2f} more.")
