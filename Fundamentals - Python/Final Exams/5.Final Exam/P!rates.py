def plunder(current_town, people_killed, gold_stolen):
    town_info[current_town]['gold'] -= gold_stolen
    town_info[current_town]['people'] -= people_killed
    print(f"{current_town} plundered! {gold_stolen} gold stolen, {people_killed} citizens killed.")
    if town_info[current_town]['gold'] == 0 or town_info[current_town]['people'] == 0:
        del town_info[current_town]
        print(f"{current_town} has been wiped off the map!")


def prosper(current_town, gold_attained):
    if gold_attained < 0:
        print("Gold added cannot be a negative number!")
        return
    town_info[current_town]['gold'] += gold_attained
    print(f"{gold_attained} gold added to the city treasury. {current_town} now has"
          f" {town_info[current_town]['gold']} gold.")


town_info = {}
information = input()
while information != "Sail":
    town, people, gold = [int(item) if item.isdigit() else item for item in information.split("||")]
    town_info[town] = town_info.get(town, {'people': 0, 'gold': 0})
    town_info[town]['people'] += people
    town_info[town]['gold'] += gold
    information = input()
command = input()
while command != "End":
    operation, town, *info = [int(item) if item[-1].isdigit() else item for item in command.split("=>")]
    if operation == "Plunder":
        plunder(town, *info)
    elif operation == "Prosper":
        prosper(town, *info)
    command = input()
if town_info:
    print(f"Ahoy, Captain! There are {len(town_info)} wealthy settlements to go to:")
    for town, value in town_info.items():
        print(f"{town} -> Population: {value['people']} citizens, Gold: {value['gold']} kg")
elif not town_info:
    print("Ahoy, Captain! All targets have been plundered and destroyed!")


# cities_resources = {}
#
# command = input()
# while command != "Sail":
#     city, population, gold = [string if string[0].isalpha() else int(string) for string in command.split("||")]
#     if city in cities_resources:
#         cities_resources[city]['population'] += population
#         cities_resources[city]['gold'] += gold
#         command = input()
#         continue
#     cities_resources[city] = cities_resources.get(city, {'population': population, 'gold': gold})
#     command = input()
#
# command = input()
# while command != "End":
#     command = command.split("=>")
#     operation, town = command[0], command[1]
#
#     if operation == "Plunder":
#         killed_people, stolen_gold = int(command[2]), int(command[3])
#         dead_people, gold_attained = 0, 0
#         if cities_resources[town]['population'] >= killed_people and cities_resources[town]['gold'] >= stolen_gold:
#             dead_people, gold_attained = killed_people, stolen_gold
#
#         if cities_resources[town]['population'] < killed_people:
#             dead_people = cities_resources[town]['population']
#
#         if cities_resources[town]['gold'] < stolen_gold:
#             gold_attained = cities_resources[town]['gold']
#
#         print(f"{town} plundered! {gold_attained} gold stolen, {dead_people} citizens killed.")
#         cities_resources[town]['population'] -= dead_people
#         cities_resources[town]['gold'] -= gold_attained
#
#         if cities_resources[town]['population'] <= 0 or cities_resources[town]['gold'] <= 0:
#             del cities_resources[town]
#             print(f"{town} has been wiped off the map!")
#
#     elif operation == "Prosper":
#         gold_increased = int(command[2])
#         if gold_increased < 0:
#             print(f"Gold added cannot be a negative number!")
#             command = input()
#             continue
#
#         cities_resources[town]['gold'] += gold_increased
#         print(f"{gold_increased} gold added to the city treasury. {town} now has {cities_resources[town]['gold']} gold.")
#
#     command = input()
#
# if cities_resources:
#     print(f"Ahoy, Captain! There are {len(cities_resources)} wealthy settlements to go to:")
#     for towns in cities_resources:
#         print(f"{towns} -> Population: {cities_resources[towns]['population']} citizens,"
#               f" Gold: {cities_resources[towns]['gold']} kg")
# else:
#     print(f"Ahoy, Captain! All targets have been plundered and destroyed!")
