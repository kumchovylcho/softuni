from math import ceil
number_of_guests = int(input())
budget = int(input())
easter_bread = 4  # enough for 3 people
egg = 0.45
number_of_easter_breads = ceil(number_of_guests / 3)
total_price_easter_breads = number_of_easter_breads * easter_bread
number_of_eggs_for_guests = (number_of_guests * 2)
total_egg_price = (number_of_guests * 2) * egg
total_price = total_price_easter_breads + total_egg_price
if budget >= total_price:
    money_left = budget - total_price
    print(f"Lyubo bought {number_of_easter_breads} Easter bread and {number_of_eggs_for_guests} eggs.")
    print(f"He has {money_left:.2f} lv. left.")
else:
    money_needed = total_price - budget
    print(f"Lyubo doesn't have enough money.\nHe needs {money_needed:.2f} lv. more.")
