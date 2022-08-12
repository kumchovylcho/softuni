kilometers = int(input())
day_or_night_travel = input()
price = 0
if kilometers < 20:
    if day_or_night_travel == "day":
        price = 0.79 * kilometers + 0.70
    else:
        price = 0.90 * kilometers + 0.70
elif kilometers < 100:
    price = 0.09 * kilometers
elif kilometers >= 100:
    price = 0.06 * kilometers
print(price)