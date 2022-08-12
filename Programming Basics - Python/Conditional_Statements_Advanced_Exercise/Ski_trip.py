days_to_stay = int(input()) - 1
room_type = input()
positive_negative = input()
price = 0
if room_type == "room for one person":
    price = 18 * days_to_stay
elif room_type == "apartment":
    price = 25 * days_to_stay
    if days_to_stay < 10:
        price *= 0.70
    elif 10 <= days_to_stay <= 15:
        price *= 0.65
    else:
        price *= 0.50
else:
    price = 35 * days_to_stay
    if days_to_stay < 10:
        price *= 0.90
    elif 10 <= days_to_stay <= 15:
        price *= 0.85
    else:
        price *= 0.80
if positive_negative == "positive":
    price *= 1.25
else:
    price *= 0.90
print(f"{price:.2f}")
