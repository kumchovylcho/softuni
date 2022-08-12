from math import ceil
number_of_people = int(input())
entering_tax = float(input())
price_per_deck_chair = float(input())
price_per_umbrella = float(input())
umbrellas = ceil((number_of_people / 2)) * price_per_umbrella
percent_75_deck_chair_wanted = ceil((number_of_people * 0.75)) * price_per_deck_chair
total_tax = number_of_people * entering_tax
total_price = umbrellas + percent_75_deck_chair_wanted + total_tax
print(f"{total_price:.2f} lv.")
