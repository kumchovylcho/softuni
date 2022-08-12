budget_of_movie = float(input())
destination = input()
season = input()
number_of_days = int(input())
price = 0
if destination == "Dubai":
    if season == "Winter":
        price = 45000 * 0.7
    else:
        price = 40000 * 0.7

elif destination == "Sofia":
    if season == "Winter":
        price = 17000 * 1.25
    else:
        price = 12500 * 1.25
else:
    if season == "Winter":
        price = 24000
    else:
        price = 20250
total_price = number_of_days * price
diff = abs(total_price - budget_of_movie)
if total_price <= budget_of_movie:
    print(f"The budget for the movie is enough! We have {diff:.2f} leva left!")
else:
    print(f"The director needs {diff:.2f} leva more!")
