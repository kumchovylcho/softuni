def add_people(people):
    wagons[-1] += people


def insert_people(index, people):
    wagons[index] += people


def people_leave(index, people):
    wagons[index] -= people


number_of_wagons = int(input())
wagons = [0] * number_of_wagons
command = input()
while command != "End":
    operation, *data = [string if string.isalpha() else int(string) for string in command.split()]
    if operation == "add":
        add_people(data[0])
    elif operation == "insert":
        insert_people(data[0], data[1])
    elif operation == "leave":
        people_leave(data[0], data[1])
    command = input()
print(wagons)




# def commands(current_command):
#     if current_command[0] == "add":
#         number_of_people = int(current_command[1])
#         result = number_of_people + int(list_with_wagons[-1])
#         list_with_wagons[-1] = result
#
#     elif current_command[0] == "insert":
#         number_of_people = int(current_command[2])
#         number_of_wagon = int(current_command[1])
#
#         result = number_of_people + int(list_with_wagons[number_of_wagon])
#         list_with_wagons[int(current_command[1])] = result
#
#     elif current_command[0] == "leave":
#         number_of_people = int(current_command[2])
#         number_of_wagon = int(current_command[1])
#
#         result = int(list_with_wagons[number_of_wagon]) - number_of_people
#         list_with_wagons[int(current_command[1])] = result
#
#
# length_of_wagons = int(input())
# list_with_wagons = [0] * length_of_wagons
# command = input()
# while command != "End":
#     commands(command.split())
#     command = input()
#
# print(list_with_wagons)
