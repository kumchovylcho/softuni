budget_for_movie = float(input())
number_of_statist = int(input())
price_for_dress_per_statist = float(input())
decor = budget_for_movie * 0.1
price_for_dress = number_of_statist * price_for_dress_per_statist
if number_of_statist > 150:
    price_for_dress *= 0.9
total_price = decor + price_for_dress
diff = abs(total_price - budget_for_movie)
if total_price > budget_for_movie:
    print("Not enough money!")
    print(f"Wingard needs {diff:.2f} leva more.")
else:
    print("Action!")
    print(f"Wingard starts filming with {diff:.2f} leva left.")
