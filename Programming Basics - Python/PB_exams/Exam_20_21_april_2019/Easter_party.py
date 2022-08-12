number_of_guests = int(input())
price_of_envelope_per_person = float(input())
budget = float(input())
price_of_cake = budget * 0.10
if 10 <= number_of_guests <= 15:
    price_of_envelope_per_person *= 0.85
elif 15 < number_of_guests <= 20:
    price_of_envelope_per_person *= 0.80
elif number_of_guests > 20:
    price_of_envelope_per_person *= 0.75
total_price = number_of_guests * price_of_envelope_per_person + price_of_cake
if total_price >= budget:
    money_left = total_price - budget
    print(f"No party! {money_left:.2f} leva needed.")
else:
    money_needed = budget - total_price
    print(f"It is party time! {money_needed:.2f} leva left.")
