def loot_chest(current_treasure_chest, *items_to_loot):
    for item in items_to_loot:
        if item not in current_treasure_chest:
            current_treasure_chest.insert(0, item)
    return current_treasure_chest


def swap_item_position(current_treasure_chest, index_of_item):
    if 0 <= index_of_item < len(current_treasure_chest):
        current_treasure_chest.append(current_treasure_chest.pop(index_of_item))
    return current_treasure_chest


def steal_items(current_treasure_chest, count_of_stolen_items):
    stolen_items = current_treasure_chest[-count_of_stolen_items:]
    current_treasure_chest = current_treasure_chest[:-count_of_stolen_items]
    print(', '.join(stolen_items))
    return current_treasure_chest


dict_operations = {
    "Loot": loot_chest,
    "Drop": swap_item_position,
    "Steal": steal_items
}
treasure_chest = input().split("|")
command = input()
while command != "Yohoho!":
    operation, *data = [item if item.isalpha() else int(item) for item in command.split()]
    if operation in dict_operations:
        treasure_chest = dict_operations[operation](treasure_chest, *data)
    command = input()
if treasure_chest:
    average_treasure_gained = sum([len(item) for item in treasure_chest]) / len(treasure_chest)
    print(f"Average treasure gain: {average_treasure_gained:.2f} pirate credits.")
else:
    print("Failed treasure hunt.")



# def loot_chest(current_chest, items_to_loot):
#     for item in items_to_loot:
#         if item not in current_chest:
#             current_chest.insert(0, item)
#     return current_chest
#
#
# def swap_item_position(current_chest, index_of_item):
#     if 0 <= index_of_item < len(current_chest):
#         current_chest.append(current_chest.pop(index_of_item))
#     return current_chest
#
#
# def steal_items(current_chest, count_of_stolen_items):
#     stolen_items = current_chest[-count_of_stolen_items:]
#     current_chest = current_chest[:-count_of_stolen_items]
#     print(', '.join(stolen_items))
#     return current_chest
#
#
# treasure_chest = input().split("|")
# command = input()
# while command != "Yohoho!":
#     operation, *data = [item if item.isalpha() else int(item) for item in command.split()]
#     if operation == "Loot":
#         treasure_chest = loot_chest(treasure_chest, data)
#     elif operation == "Drop":
#         treasure_chest = swap_item_position(treasure_chest, data[0])
#     elif operation == "Steal":
#         treasure_chest = steal_items(treasure_chest, data[0])
#     command = input()
# if treasure_chest:
#     average_treasure_gained = sum([len(item) for item in treasure_chest]) / len(treasure_chest)
#     print(f"Average treasure gain: {average_treasure_gained:.2f} pirate credits.")
# else:
#     print("Failed treasure hunt.")



# def loot(items):
#     del items[0]    # deleting the command , so it doesn't loop it too
#     for item in items:
#         if item not in loot_in_chest:
#             loot_in_chest.insert(0, item)     # puts the current_shard at zero current_index
#
#
# def drop(index):
#     index = int(index[1])  # making it from str to int
#     if abs(index) < len(loot_in_chest):   # checking if the current_index is in the range of the shuffled_cards
#         loot_in_chest.append(loot_in_chest.pop(index))
#
#
# def steal(number_of_times):
#     global loot_in_chest
#     count_items = int(number_of_times[1])
#     stolen_items = loot_in_chest[-count_items:]
#     loot_in_chest = loot_in_chest[:-count_items]
#     print(*stolen_items, sep=", ")
#
#
# loot_in_chest = input().split("|")
# command = input()
# while command != "Yohoho!":
#     if "Loot" in command:
#         loot(command.split())
#     elif "Drop" in command:
#         drop(command.split())
#     elif "Steal" in command:
#         steal(command.split())
#     command = input()
#
# points_of_length_items = 0
# for item in loot_in_chest:
#     points_of_length_items += len(item)
#
#
# if len(loot_in_chest) > 0:
#     average_treasure_gain = points_of_length_items / len(loot_in_chest)
#     print(f"Average treasure gain: {average_treasure_gain:.2f} pirate credits.")
# elif len(loot_in_chest) == 0:
#     print("Failed treasure hunt.")
