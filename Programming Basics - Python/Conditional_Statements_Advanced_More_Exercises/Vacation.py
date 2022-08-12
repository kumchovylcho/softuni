budget = float(input())
season = input()
location = ""
place_to_stay = ""
price = budget
if budget <= 1000:
    place_to_stay = "Camp"
    if season == "Summer":
        price *= 0.65
        location = "Alaska"
    else:
        price *= 0.45
        location = "Morocco"
elif 1000 < budget <= 3000:
    place_to_stay = "Hut"
    if season == "Summer":
        price *= 0.80
        location = "Alaska"
    else:
        price *= 0.60
        location = "Morocco"
else:
    price *= 0.90
    place_to_stay = "Hotel"
    if season == "Summer":
        location = "Alaska"
    else:
        location = "Morocco"
print(f"{location} - {place_to_stay} - {price:.2f}")
