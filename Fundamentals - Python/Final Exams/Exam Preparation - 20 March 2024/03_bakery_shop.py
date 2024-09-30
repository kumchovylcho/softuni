def stocks() -> tuple[dict[str, int], int]:
    shop_stocks = {}
    sold_stocks = 0

    command = input()
    while command != END_OF_COMMANDS:
        operation, quantity, food = command.split()
        quantity = int(quantity)

        if operation == "Receive" and quantity > 0:
            shop_stocks[food] = shop_stocks.get(food, 0) + quantity
        elif operation == "Sell":
            if food not in shop_stocks:
                print(f"You do not have any {food}.")
                command = input()
                continue

            in_stock = shop_stocks[food]
            if quantity > in_stock:
                sold_stocks += in_stock
                print(f"There aren't enough {food}. You sold the last {in_stock} of them.")
            elif quantity <= in_stock:
                sold_stocks += quantity
                print(f"You sold {quantity} {food}.")

            shop_stocks[food] -= quantity
            if shop_stocks[food] <= 0:
                shop_stocks.pop(food)

        command = input()

    return shop_stocks, sold_stocks


END_OF_COMMANDS = "Complete"
shop_items, sold_items = stocks()

for food, quantity in shop_items.items():
    print(f"{food}: {quantity}")
print(f"All sold: {sold_items} goods")