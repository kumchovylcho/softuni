name_of_movie = input()
type_of_movie_room = input()
number_of_purchased_tickets = int(input())
price = 0
if type_of_movie_room == "normal":
    if name_of_movie == "A Star Is Born":
        price = 7.50
    elif name_of_movie == "Bohemian Rhapsody":
        price = 7.35
    elif name_of_movie == "Green Book":
        price = 8.15
    else:
        price = 8.75
elif type_of_movie_room == "luxury":
    if name_of_movie == "A Star Is Born":
        price = 10.50
    elif name_of_movie == "Bohemian Rhapsody":
        price = 9.45
    elif name_of_movie == "Green Book":
        price = 10.25
    else:
        price = 11.55
else:
    if name_of_movie == "A Star Is Born":
        price = 13.50
    elif name_of_movie == "Bohemian Rhapsody":
        price = 12.75
    elif name_of_movie == "Green Book":
        price = 13.25
    else:
        price = 13.95
total_price = price * number_of_purchased_tickets
print(f"{name_of_movie} -> {total_price:.2f} lv.")
