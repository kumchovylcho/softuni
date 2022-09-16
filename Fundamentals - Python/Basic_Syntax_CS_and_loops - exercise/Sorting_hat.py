houses = {
    'Gryffindor': 5,
    'Slytherin': 6,
    'Ravenclaw': 7,
    'Hufflepuff': 15
}
name = input()
while name != "Welcome!":
    if name == "Voldemort":
        print("You must not speak of that name!")
        break
    for house, points in houses.items():
        if len(name) < points:
            print(f"{name} goes to {house}.")
            break
    name = input()
else:
    print("Welcome to Hogwarts.")


# current_name = input()
# while current_name != "Welcome!":
#     if current_name == "Voldemort":
#         print("You must not speak of that name!")
#         break
#     if len(current_name) < 5:
#         print(f"{current_name} goes to Gryffindor.")
#     elif len(current_name) == 5:
#         print(f"{current_name} goes to Slytherin.")
#     elif len(current_name) == 6:
#         print(f"{current_name} goes to Ravenclaw.")
#     elif len(current_name) > 6:
#         print(f"{current_name} goes to Hufflepuff.")
#     current_name = input()
# if current_name == "Welcome!":
#     print("Welcome to Hogwarts.")
