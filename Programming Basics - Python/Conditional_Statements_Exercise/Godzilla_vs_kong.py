movie_budget = float(input())
number_of_statist = int(input())
price_of_cloth_for_one_statist = float(input())
decor = movie_budget * 0.10
price_of_clothes = number_of_statist * price_of_cloth_for_one_statist
if number_of_statist > 150:
    price_of_clothes *= 0.90
total = decor + price_of_clothes
if movie_budget >= total:
    diff = movie_budget - total
    print(f"Action!\nWingard starts filming with {diff:.2f} leva left.")
else:
    diff = total - movie_budget
    print(f"Not enough money!\nWingard needs {diff:.2f} leva more.")
