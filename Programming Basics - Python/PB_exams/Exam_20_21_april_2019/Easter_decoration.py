total_price = 0
all_money = 0
number_of_products = 0
number_of_customers = int(input())
for customers in range(1, number_of_customers + 1):
    product = input()
    while product != "Finish":
        number_of_products += 1
        if product == "basket":
            total_price += 1.50
        elif product == "wreath":
            total_price += 3.80
        else:
            total_price += 7
        product = input()
    if number_of_products % 2 == 0:
        total_price *= 0.8
    print(f"You purchased {number_of_products} items for {total_price:.2f} leva.")
    number_of_products = 0
    all_money += total_price
    total_price = 0
average_bill = all_money / number_of_customers
print(f"Average bill per client is: {average_bill:.2f} leva.")
