ticket_price = 150
items = input().split("|")
budget = float(input())

bought_items = []
profit = 0

for pair in items:
    item, price = [float(x) if x[-1].isdigit() else x for x in pair.split("->")]

    if budget >= price:
        if any(item == product and price <= product_price
               for product, product_price in (("Clothes", 50),
                                              ("Shoes", 35),
                                              ("Accessories", 20.5))):
            budget -= price
            bought_items.append(price * 1.4)
            profit += bought_items[-1] - price


print(" ".join(f"{x:.2f}" for x in bought_items))
print(f"Profit: {profit:.2f}")
print("Hello, France!" if budget + sum(bought_items) >= ticket_price else "Not enough money.")


# items_with_prices = input().split("|")
# budget = float(input())
# profit = 0
# bought_items = []
# sold_items = []
# for item in items_with_prices:
#     item_list = item.split("->")
#     price_of_item = float(item_list[1])
#     category_of_item = item_list[0]
#     if budget >= price_of_item:
#         if category_of_item == "Clothes" and price_of_item <= 50 or \
#              category_of_item == "Shoes" and price_of_item <= 35 or \
#              category_of_item == "Accessories" and price_of_item <= 20.5:
#             budget -= price_of_item
#             bought_items.append(price_of_item)
# for price in bought_items:
#     profit += price * 0.40
#     sold_items.append(price + (price * 0.4))
# for price in sold_items:
#     print(f"{price:.2f}", end=" ")
# print(f"\nProfit: {profit:.2f}")
# if sum(sold_items) + budget >= 150:
#     print("Hello, France!")
# else:
#     print("Not enough money.")
