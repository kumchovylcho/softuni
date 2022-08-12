from math import ceil
name_of_the_football_fan = input()
budget = float(input())
beer_bottles = int(input())
packages_of_chips = int(input())
price_for_beers = beer_bottles * 1.20
price_for_chips = ceil(packages_of_chips * (price_for_beers * 0.45))
total_price = price_for_chips + price_for_beers
diff = abs(total_price - budget)
if total_price <= budget:
    print(f"{name_of_the_football_fan} bought a snack and has {diff:.2f} leva left.")
else:
    print(f"{name_of_the_football_fan} needs {diff:.2f} more leva!")
