products_in_stock = input().split()
wanted_products = input().split()
stock_items = dict()

for item in range(0, len(products_in_stock), 2):
    product = products_in_stock[item]
    quantity = int(products_in_stock[item + 1])
    stock_items[product] = quantity

for product in wanted_products:
    if product not in stock_items:
        print(f"Sorry, we don't have {product}")
    elif product in stock_items:
        print(f"We have {stock_items[product]} of {product} left")
