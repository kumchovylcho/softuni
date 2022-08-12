budget = float(input())
money_left = budget
product_counter = 0
total = 0
product = input()
while product != "Stop":
    price_of_product = float(input())
    product_counter += 1
    if product_counter % 3 == 0:
        price_of_product /= 2
    if money_left < price_of_product:
        diff = price_of_product - money_left
        print(f"You don't have enough money!\nYou need {diff:.2f} leva!")
        break
    money_left -= price_of_product
    product = input()
if product == "Stop":
    print(f"You bought {product_counter} products for {budget - money_left:.2f} leva.")
