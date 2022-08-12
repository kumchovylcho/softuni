name_of_city = input()
type_of_package = input()
is_VIP = input()
days_to_stay = int(input())
cities = "Bansko", "Borovets", "Varna", "Burgas"
packages = "noEquipment", "withEquipment", "noBreakfast", "withBreakfast"
price = 0
if name_of_city == "Bansko" or name_of_city == "Borovets":
    if type_of_package == "withEquipment":
        price = 100
        if is_VIP == "yes":
            price *= 0.90
    else:
        price = 80
        if is_VIP == "yes":
            price *= 0.95
elif name_of_city == "Varna" or name_of_city == "Burgas":
    if type_of_package == "withBreakfast":
        price = 130
        if is_VIP == "yes":
            price *= 0.88
    else:
        price = 100
        if is_VIP == "yes":
            price *= 0.93
if name_of_city not in cities or type_of_package not in packages:
    print("Invalid input!")
elif days_to_stay < 1:
    print("Days must be positive digit!")
else:
    total_price = price * days_to_stay
    if days_to_stay > 7:
        total_price = price * (days_to_stay - 1)
        print(f"The price is {total_price:.2f}lv! Have a nice time!")
    else:
        print(f"The price is {total_price:.2f}lv! Have a nice time!")
