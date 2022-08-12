capacity_of_room = int(input())
capacity_of_room_left = capacity_of_room
ticket = 5
total = 0
number_of_people_entering = input()
while number_of_people_entering != "Movie time!":
    number_of_people_entering = int(number_of_people_entering)
    if number_of_people_entering > capacity_of_room_left:
        print(f"The cinema is full.\nCinema income - {total} lv.")
        break
    if number_of_people_entering % 3 == 0:
        total += (number_of_people_entering * ticket) - 5
    else:
        total += number_of_people_entering * ticket
    capacity_of_room_left -= number_of_people_entering
    number_of_people_entering = input()
else: #number_of_people_entering == "Movie time!":
    print(f"There are {capacity_of_room_left} seats left in the cinema.\nCinema income - {total} lv.")
