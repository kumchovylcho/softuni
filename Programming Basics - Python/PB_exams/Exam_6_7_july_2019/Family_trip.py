budget = float(input())
number_of_nights = int(input())
price_per_night = float(input())
percent_extra_costs = int(input())
if number_of_nights > 7:
    price_per_night *= 0.95
total_price = number_of_nights * price_per_night
total = ((percent_extra_costs / 100) * budget) + total_price
diff = budget - total
if diff >= 0:
    print(f"Ivanovi will be left with {diff:.2f} leva after vacation.")
else:
    print(f"{abs(diff):.2f} leva needed.")
