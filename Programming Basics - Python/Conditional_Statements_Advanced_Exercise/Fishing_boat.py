budget = int(input())
season = input()
fishermen_count = int(input())
price = 0
if season == "Spring":
    price = 3000
elif season == "Winter":
    price = 2600
else:
    price = 4200
if fishermen_count <= 6:
    price *= 0.90
elif 7 <= fishermen_count <= 11:
    price *= 0.85
else:
    price *= 0.75
if fishermen_count % 2 == 0 and season != "Autumn":
    price *= 0.95
diff = abs(price - budget)
if price <= budget:
    print(f"Yes! You have {diff:.2f} leva left.")
else:
    print(f"Not enough money! You need {diff:.2f} leva.")
