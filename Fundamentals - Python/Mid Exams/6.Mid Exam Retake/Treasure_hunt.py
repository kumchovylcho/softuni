loot_in_chest = input().split("|")


def loot(items):
    del items[0]    # deleting the command , so it doesn't loop it too
    for item in items:
        if item not in loot_in_chest:
            loot_in_chest.insert(0, item)     # puts the current_shard at zero current_index


def drop(index):
    index = int(index[1])  # making it from str to int
    if abs(index) < len(loot_in_chest):   # checking if the current_index is in the range of the list
        loot_in_chest.append(loot_in_chest.pop(index))


def steal(number_of_times):
    global loot_in_chest
    count_items = int(number_of_times[1])
    stolen_items = loot_in_chest[-count_items:]
    loot_in_chest = loot_in_chest[:-count_items]
    print(*stolen_items, sep=", ")


command = input()
while command != "Yohoho!":
    if "Loot" in command:
        loot(command.split())
    elif "Drop" in command:
        drop(command.split())
    elif "Steal" in command:
        steal(command.split())
    command = input()

points_of_length_items = 0
for item in loot_in_chest:
    points_of_length_items += len(item)


if len(loot_in_chest) > 0:
    average_treasure_gain = points_of_length_items / len(loot_in_chest)
    print(f"Average treasure gain: {average_treasure_gain:.2f} pirate credits.")
elif len(loot_in_chest) == 0:
    print("Failed treasure hunt.")
