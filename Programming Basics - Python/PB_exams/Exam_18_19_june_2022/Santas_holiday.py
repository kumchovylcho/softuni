number_of_days = int(input()) - 1
type_of_room = input()
grade = input()
price = 0
if type_of_room == "room for one person":
    price = 18 * number_of_days
elif type_of_room == "apartment":
    price = 25 * number_of_days
    if number_of_days < 10:
        price *= 0.7
    elif 10 <= number_of_days < 15:
        price *= 0.65
    else:
        price *= 0.50
else:
    price = 35 * number_of_days
    if number_of_days < 10:
        price *= 0.9
    elif 10 <= number_of_days < 15:
        price *= 0.85
    else:
        price *= 0.8
if grade == "positive":
    price *= 1.25
else:
    price *= 0.9
print(f"{price:.2f}")
