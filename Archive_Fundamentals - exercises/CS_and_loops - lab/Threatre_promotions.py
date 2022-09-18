type_of_day, age = input(), int(input())
ticket_price = 0
if type_of_day == "Weekday":
    if 0 <= age <= 18 or 64 < age <= 122:
        ticket_price = 12
    elif 18 < age <= 64:
        ticket_price = 18
elif type_of_day == "Weekend":
    if 0 <= age <= 18 or 64 < age <= 122:
        ticket_price = 15
    elif 18 < age <= 64:
        ticket_price = 20
elif type_of_day == "Holiday":
    if 0 <= age <= 18:
        ticket_price = 5
    elif 18 < age <= 64:
        ticket_price = 12
    elif 64 < age <= 122:
        ticket_price = 10
if ticket_price:
    print(f"{ticket_price}$")
else:
    print("Error!")

# type_of_day, age = input(), int(input())
# ticket_price = 0
# if (0 <= age <= 18 or 64 < age <= 122) and type_of_day == "Weekday":
#     ticket_price = 12
# elif 18 < age <= 64 and type_of_day == "Weekday":
#     ticket_price = 18
#
# elif (0 <= age <= 18 or 64 < age <= 122) and type_of_day == "Weekend":
#     ticket_price = 15
# elif 18 < age <= 64 and type_of_day == "Weekend":
#     ticket_price = 20
#
# elif 0 <= age <= 18 and type_of_day == "Holiday":
#     ticket_price = 5
# elif 18 < age <= 64 and type_of_day == "Holiday":
#     ticket_price = 12
# elif 64 < age <= 122 and type_of_day == "Holiday":
#     ticket_price = 10
#
# if ticket_price:
#     print(f"{ticket_price}$")
# else:
#     print("Error!")
