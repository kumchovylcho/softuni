season = input()
type_of_group = input()
number_of_students = int(input())
number_of_nights = int(input())
price = 0
sport = ""
if season == "Winter":
    if type_of_group == "boys":
        sport = "Judo"
        price = 9.60
    elif type_of_group == "girls":
        sport = "Gymnastics"
        price = 9.60
    else:
        sport = "Ski"
        price = 10
elif season == "Spring":
    if type_of_group == "boys":
        sport = "Tennis"
        price = 7.20
    elif type_of_group == "girls":
        sport = "Athletics"
        price = 7.20
    else:
        sport = "Cycling"
        price = 9.50
elif season == "Summer":
    if type_of_group == "boys":
        sport = "Football"
        price = 15
    elif type_of_group == "girls":
        sport = "Voleyball"
        price = 15
    else:
        sport = "Swimming"
        price = 20
total = (price * number_of_students) * number_of_nights
if 10 <= number_of_students < 20:
    total *= 0.95
elif 20 <= number_of_students < 50:
    total *= 0.85
elif number_of_students >= 50:
    total *= 0.50
print(f"{sport} {total:.2f} lv.")
