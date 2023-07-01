def check_for_null_values(damage, health, armor):
    if damage == "null":
        damage = 45

    if health == "null":
        health = 250

    if armor == "null":
        armor = 10

    return damage, health, armor


number_of_dragons = int(input())
dragons = {}

for _ in range(number_of_dragons):
    color, name, damage, health, armor = [x if x.isalpha() else int(x) for x in input().split()]

    damage, health, armor = check_for_null_values(damage, health, armor)

    dragons[color] = dragons.get(color, {})
    dragons[color][name] = {"damage": damage, "health": health, "armor": armor}


for color in dragons:

    total_dragons_in_color = len(dragons[color])
    avg_damage, avg_health, avg_armor = 0, 0, 0
    for stats in dragons[color].values():
        avg_damage += stats["damage"]
        avg_health += stats["health"]
        avg_armor += stats["armor"]

    avg_damage /= total_dragons_in_color
    avg_health /= total_dragons_in_color
    avg_armor /= total_dragons_in_color

    print(f"{color}::({avg_damage:.2f}/{avg_health:.2f}/{avg_armor:.2f})")
    for name, stats in sorted(dragons[color].items()):
        print(f"-{name} -> damage: {stats['damage']}, health: {stats['health']}, armor: {stats['armor']}")


########################################################################################################


# def create_dragon(colour, dragon_name, dmg, hp, defense, all_dragons_dict):
#     all_dragons_dict[colour] = all_dragons_dict.get(colour, {})
#     all_dragons_dict[colour][dragon_name] = {'dmg': dmg, 'hp': hp, 'defense': defense}
#     return all_dragons_dict
#
#
# def show_results(all_dragons):
#     for colour in all_dragons:
#         average_dmg, average_hp, average_armor = 0, 0, 0
#         for dragon_name in all_dragons[colour]:
#             average_dmg += all_dragons[colour][dragon_name]['dmg']
#             average_hp += all_dragons[colour][dragon_name]['hp']
#             average_armor += all_dragons[colour][dragon_name]['defense']
#         all_dragons_per_color = len(all_dragons[colour])
#         print(f"{colour}::({average_dmg / all_dragons_per_color:.2f}/{average_hp / all_dragons_per_color:.2f}/"
#               f"{average_armor / all_dragons_per_color:.2f})")
#         for dragon_name in sorted(all_dragons[colour]):
#             print(f"-{dragon_name} -> damage: {all_dragons[colour][dragon_name]['dmg']},"
#                   f" health: {all_dragons[colour][dragon_name]['hp']},"
#                   f" armor: {all_dragons[colour][dragon_name]['defense']}")
#
#
# dragons = {}
# dragons_count = int(input())
# for add_dragon in range(dragons_count):
#     current_dragon = input().split()
#     color, name, damage, health, armor = [int(item) if item.isdigit() else item for item in current_dragon]
#     if damage == 'null':
#         damage = 45
#     if health == 'null':
#         health = 250
#     if armor == 'null':
#         armor = 10
#     create_dragon(color, name, damage, health, armor, dragons)
# show_results(dragons)
