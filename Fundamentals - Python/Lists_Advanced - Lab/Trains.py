length_of_wagons = int(input())
list_with_wagons = [0] * length_of_wagons


def commands(current_command):
    if current_command[0] == "add":
        number_of_people = int(current_command[1])
        result = number_of_people + int(list_with_wagons[-1])
        list_with_wagons[-1] = result

    elif current_command[0] == "insert":
        number_of_people = int(current_command[2])
        number_of_wagon = int(current_command[1])

        result = number_of_people + int(list_with_wagons[number_of_wagon])
        list_with_wagons[int(current_command[1])] = result

    elif current_command[0] == "leave":
        number_of_people = int(current_command[2])
        number_of_wagon = int(current_command[1])

        result = int(list_with_wagons[number_of_wagon]) - number_of_people
        list_with_wagons[int(current_command[1])] = result


command = input()
while command != "End":
    commands(command.split())
    command = input()

print(list_with_wagons)
