cities_resources = {}

command = input()
while command != "Sail":
    city, population, gold = [string if string[0].isalpha() else int(string) for string in command.split("||")]
    if city in cities_resources:
        cities_resources[city]['population'] += population
        cities_resources[city]['gold'] += gold
        command = input()
        continue
    cities_resources[city] = cities_resources.get(city, {'population': population, 'gold': gold})
    command = input()

command = input()
while command != "End":
    command = command.split("=>")
    operation, town = command[0], command[1]

    if operation == "Plunder":
        killed_people, stolen_gold = int(command[2]), int(command[3])
        dead_people, gold_attained = 0, 0
        if cities_resources[town]['population'] >= killed_people and cities_resources[town]['gold'] >= stolen_gold:
            dead_people, gold_attained = killed_people, stolen_gold

        if cities_resources[town]['population'] < killed_people:
            dead_people = cities_resources[town]['population']

        if cities_resources[town]['gold'] < stolen_gold:
            gold_attained = cities_resources[town]['gold']

        print(f"{town} plundered! {gold_attained} gold stolen, {dead_people} citizens killed.")
        cities_resources[town]['population'] -= dead_people
        cities_resources[town]['gold'] -= gold_attained

        if cities_resources[town]['population'] <= 0 or cities_resources[town]['gold'] <= 0:
            del cities_resources[town]
            print(f"{town} has been wiped off the map!")

    elif operation == "Prosper":
        gold_increased = int(command[2])
        if gold_increased < 0:
            print(f"Gold added cannot be a negative number!")
            command = input()
            continue

        cities_resources[town]['gold'] += gold_increased
        print(f"{gold_increased} gold added to the city treasury. {town} now has {cities_resources[town]['gold']} gold.")

    command = input()

if cities_resources:
    print(f"Ahoy, Captain! There are {len(cities_resources)} wealthy settlements to go to:")
    for towns in cities_resources:
        print(f"{towns} -> Population: {cities_resources[towns]['population']} citizens,"
              f" Gold: {cities_resources[towns]['gold']} kg")
else:
    print(f"Ahoy, Captain! All targets have been plundered and destroyed!")
