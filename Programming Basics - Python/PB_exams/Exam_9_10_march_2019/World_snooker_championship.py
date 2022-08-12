stage_of_championship = input()
type_ticket = input()
number_of_tickets = int(input())
photo_with_trophy = input()
ticket_price = 0
if stage_of_championship == "Quarter final":
    if type_ticket == "Standard":
        ticket_price = 55.50
    elif type_ticket == "Premium":
        ticket_price = 105.20
    else:
        ticket_price = 118.90
elif stage_of_championship == "Semi final":
    if type_ticket == "Standard":
        ticket_price = 75.88
    elif type_ticket == "Premium":
        ticket_price = 125.22
    else:
        ticket_price = 300.40
else:
    if type_ticket == "Standard":
        ticket_price = 110.10
    elif type_ticket == "Premium":
        ticket_price = 160.66
    else:
        ticket_price = 400
total = ticket_price * number_of_tickets
if 2500 < total <= 4000:
    total *= 0.90
    if photo_with_trophy == "Y":
        total = total + number_of_tickets * 40
elif total > 4000:
    total *= 0.75
else:
    if photo_with_trophy == "Y":
        total += number_of_tickets * 40

print(f"{total:.2f}")
