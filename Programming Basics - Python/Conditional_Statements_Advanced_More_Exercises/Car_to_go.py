budget = float(input())
season = input()
type_car = ""
class_car = ""
price = budget
if budget <= 100:
    class_car = "Economy class"
    if season == "Summer":
        price *= 0.35
        type_car = "Cabrio"
    else:
        price *= 0.65
        type_car = "Jeep"
elif 100 < budget <= 500:
    class_car = "Compact class"
    if season == "Summer":
        price *= 0.45
        type_car = "Cabrio"
    else:
        price *= 0.80
        type_car = "Jeep"
else:
    class_car = "Luxury class"
    price *= 0.90
    type_car = "Jeep"
print(f"{class_car}\n{type_car} - {price:.2f}")
