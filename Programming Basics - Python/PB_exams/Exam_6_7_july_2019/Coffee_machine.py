drink = input()
sugar = input()
number_of_drinks = int(input())
if drink == "Espresso" and sugar == "Normal":
    price = 1
    if number_of_drinks >= 5:
        price *= 0.75
elif drink == "Cappuccino" and sugar == "Normal":
    price = 1.20
elif drink == "Tea" and sugar == "Normal":
    price = 0.60
elif drink == "Espresso" and sugar == "Extra":
    price = 1.20
    if number_of_drinks >= 5:
        price *= 0.75
elif drink == "Cappuccino" and sugar == "Extra":
    price = 1.60
elif drink == "Tea" and sugar == "Extra":
    price = 0.70
else:
    if drink == "Espresso":
        price = 0.90 * 0.65
        if number_of_drinks >= 5:
            price *= 0.75
    elif drink == "Cappuccino":
        price = 1 * 0.65
    else:
        price = 0.50 * 0.65
total_price = price * number_of_drinks
if total_price > 15:
    total_price *= 0.80
print(f"You bought {number_of_drinks} cups of {drink} for {total_price:.2f} lv.")