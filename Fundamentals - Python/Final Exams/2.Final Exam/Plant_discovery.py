discovered_plants = int(input())
all_plants = {}

for adding_plants in range(discovered_plants):
    current_plant, rarity = [int(rarity) if rarity.isdigit() else rarity for rarity in input().split("<->")]
    if current_plant in all_plants:
        all_plants[current_plant]['rarity'] = rarity
        continue
    all_plants[current_plant] = all_plants.get(current_plant, {'rarity': rarity, 'rating': []})

command = input()
while command != "Exhibition":
    command = command.split()
    command_type, current_plant = command[0], command[1]

    if current_plant not in all_plants:
        print("error")
        command = input()
        continue

    if command_type == "Rate:":
        rating = int(command[3])
        all_plants[current_plant]['rating'].append(rating)

    elif command_type == "Update:":
        rarity = int(command[3])
        all_plants[current_plant]['rarity'] = rarity

    elif command_type == "Reset:":
        all_plants[current_plant]['rating'] = []
    command = input()

print("Plants for the exhibition:")
for plants in all_plants:
    rarity = all_plants[plants]['rarity']
    rating = 0
    if len(all_plants[plants]['rating']):
        rating = sum(all_plants[plants]['rating']) / len(all_plants[plants]['rating'])
    print(f"- {plants}; Rarity: {rarity}; Rating: {rating:.2f}")