travel_place = input()


def main():
    command = input()
    while command != "Travel":
        command = command.split(":")
        if "Add" in command[0]:
            add(int(command[1]), command[2])

        elif "Remove" in command[0]:
            remove(int(command[1]), int(command[2]))

        elif command[0] == "Switch":
            switch(command[1], command[2])

        print(travel_place)
        command = input()
    print(f"Ready for world tour! Planned stops: {travel_place}")


def add(index, string):
    global travel_place
    if 0 <= index < len(travel_place):
        travel_place = f"{travel_place[:index]}{string}{travel_place[index:]}"


def remove(start_index, end_index):
    global travel_place
    if 0 <= start_index and end_index < len(travel_place):
        travel_place = f"{travel_place[:start_index]}{travel_place[end_index + 1:]}"   # ending_index is  + 1 to jump over the last letter of the word


def switch(old_string, new_string):
    global travel_place
    if old_string in travel_place:
        travel_place = travel_place.replace(old_string, new_string)


main()


# travel_place = input()
#
# command = input()
# while command != "Travel":
#     command = command.split(":")
#
#     if "Add" in command[0]:
#         string = command[2]
#         index = int(command[1])
#         if 0 <= index < len(travel_place):
#             travel_place = f"{travel_place[:index]}{string}{travel_place[index:]}"
#
#     elif "Remove" in command[0]:
#         start_index = int(command[1])
#         end_index = int(command[2])   # you can't put end_index + 1 here , since it might not get into the if statement
#         if 0 <= start_index and end_index < len(travel_place):
#             travel_place = f"{travel_place[:start_index]}{travel_place[end_index + 1:]}"   # ending_index is  + 1 to jump over the last letter of the word
#
#     elif command[0] == "Switch":
#         old_string = command[1]
#         new_string = command[2]
#         if old_string in travel_place:
#             travel_place = travel_place.replace(old_string, new_string)
#
#     print(travel_place)
#     command = input()
#
# print(f"Ready for world tour! Planned stops: {travel_place}")
