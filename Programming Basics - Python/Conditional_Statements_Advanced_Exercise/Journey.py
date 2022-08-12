budget = float(input())
season = input()
price = budget
place = ""
destination = ""
if budget <= 100:
    destination = "Bulgaria"
    if season == "summer":
        price *= 0.30
        place = "Camp"
    else:
        price *= 0.70
        place = "Hotel"
elif budget <= 1000:
    destination = "Balkans"
    if season == "summer":
        price *= 0.4
        place = "Camp"
    else:
        price *= 0.8
        place = "Hotel"
else:
    destination = "Europe"
    place = "Hotel"
    price *= 0.9

print(f"Somewhere in {destination}\n{place} - {price:.2f}")
