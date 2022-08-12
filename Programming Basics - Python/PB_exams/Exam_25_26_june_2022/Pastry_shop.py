sweet = input()
number_of_sweets = int(input())
day_of_the_month = int(input())
price = 0
total_price = 0
if day_of_the_month <= 15:
    if sweet == "Cake":
        price = 24
    elif sweet == "Souffle":
        price = 6.66
    elif sweet == "Baklava":
        price = 12.60
elif 15 < day_of_the_month <= 22 or 22 < day_of_the_month <= 24:
    if sweet == "Cake":
        price = 28.70
    elif sweet == "Souffle":
        price = 9.80
    elif sweet == "Baklava":
        price = 16.98
total_price += price * number_of_sweets
if 22 < day_of_the_month <= 24:
    print(f"{total_price:.2f}")
else:
    if 100 <= total_price <= 200:
        total_price *= 0.85
    elif total_price > 200:
        total_price *= 0.75
    if day_of_the_month <= 15:
        total_price *= 0.9
    print(f"{total_price:.2f}")
