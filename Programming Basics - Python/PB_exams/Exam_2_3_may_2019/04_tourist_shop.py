budget = float(input())
bought_items = 0
total_price = 0

item = input()
while item != "Stop":
    price = float(input())

    bought_items += 1
    if bought_items % 3 == 0:
        price *= 0.5

    if price > budget:
        print("You don't have enough money!")
        print(f"You need {abs(budget - price):.2f} leva!")
        break

    budget -= price
    total_price += price

    item = input()

else:
    print(f"You bought {bought_items} products for {total_price:.2f} leva.")

#########################################################################################

# budget = float(input())
# money_left = budget
# product_counter = 0
# total = 0
# product = input()
# while product != "Stop":
#     price_of_product = float(input())
#     product_counter += 1
#     if product_counter % 3 == 0:
#         price_of_product /= 2
#     if money_left < price_of_product:
#         diff = price_of_product - money_left
#         print(f"You don't have enough money!\nYou need {diff:.2f} leva!")
#         break
#     money_left -= price_of_product
#     product = input()
# if product == "Stop":
#     print(f"You bought {product_counter} products for {budget - money_left:.2f} leva.")
