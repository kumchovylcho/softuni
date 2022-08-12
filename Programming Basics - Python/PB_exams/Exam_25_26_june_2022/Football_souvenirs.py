team = input()
souvenirs = input()
bought_souvenirs = int(input())
countries = "Argentina", "Brazil", "Croatia", "Denmark"
souvenir_items = "flags", "caps", "posters", "stickers"
price = 0
if team == "Argentina":
    if souvenirs == "flags":
        price = 3.25
    elif souvenirs == "caps":
        price = 7.20
    elif souvenirs == "posters":
        price = 5.10
    elif souvenirs == "stickers":
        price = 1.25
elif team == "Brazil":
    if souvenirs == "flags":
        price = 4.20
    elif souvenirs == "caps":
        price = 8.50
    elif souvenirs == "posters":
        price = 5.35
    elif souvenirs == "stickers":
        price = 1.20
elif team == "Croatia":
    if souvenirs == "flags":
        price = 2.75
    elif souvenirs == "caps":
        price = 6.90
    elif souvenirs == "posters":
        price = 4.95
    elif souvenirs == "stickers":
        price = 1.10
elif team == "Denmark":
    if souvenirs == "flags":
        price = 3.10
    elif souvenirs == "caps":
        price = 6.50
    elif souvenirs == "posters":
        price = 4.80
    elif souvenirs == "stickers":
        price = 0.90
if team not in countries:
    print("Invalid country!")
elif souvenirs not in souvenir_items:
    print("Invalid stock!")
else:
    total_price = price * bought_souvenirs
    print(f"Pepi bought {bought_souvenirs} {souvenirs} of {team} for {total_price:.2f} lv.")
