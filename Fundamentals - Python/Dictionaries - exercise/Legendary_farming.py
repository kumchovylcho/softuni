shards = {
    "legendary": {
        "shards": 0,
        "fragments": 0,
        "motes": 0},
    "junk": {}
}

shadowmourne = False
valanyr = False
dragonwrath = False

while not shadowmourne and not valanyr and not dragonwrath:
    loot_table = input().split()
    for loot in range(0, len(loot_table), 2):
        quantity = int(loot_table[loot])
        item_name = loot_table[loot + 1].lower()

        if item_name in shards["legendary"]:
            shards["legendary"][item_name] += quantity

            if shards["legendary"]["shards"] >= 250:
                shadowmourne = True
                print("Shadowmourne obtained!")
                shards["legendary"]["shards"] -= 250
            elif shards["legendary"]["fragments"] >= 250:
                valanyr = True
                print("Valanyr obtained!")
                shards["legendary"]["fragments"] -= 250
            elif shards["legendary"]["motes"] >= 250:
                dragonwrath = True
                print("Dragonwrath obtained!")
                shards["legendary"]["motes"] -= 250
        elif item_name not in shards["junk"]:
            shards["junk"][item_name] = quantity
        elif item_name in shards["junk"]:
            shards["junk"][item_name] += quantity

        if shadowmourne or valanyr or dragonwrath:
            break

[print(f"{shard}: {shards['legendary'][shard]}") for shard in shards["legendary"]]

[print(f"{junk}: {shards['junk'][junk]}") for junk in shards["junk"]]


# legendary_items = {"shards": 0,
#                    "fragments": 0,
#                    "motes": 0
#                    }
#
# shadowmourne = False
# valanyr = False
# dragonwrath = False
#
#
# def check_for_items():
#     global shadowmourne
#     global valanyr
#     global dragonwrath
#     if legendary_items["shards"] >= 250:
#         legendary_items["shards"] -= 250
#         print("Shadowmourne obtained!")
#         shadowmourne = True
#
#     elif legendary_items["fragments"] >= 250:
#         legendary_items["fragments"] -= 250
#         print("Valanyr obtained!")
#         valanyr = True
#
#     elif legendary_items["motes"] >= 250:
#         legendary_items["motes"] -= 250
#         print("Dragonwrath obtained!")
#         dragonwrath = True
#
#
# while not shadowmourne and not valanyr and not dragonwrath:
#     loot_table = input().split()
#
#     for loot in range(0, len(loot_table), 2):
#         quantity = int(loot_table[loot])
#         current_shard = loot_table[loot + 1].lower()
#
#         if current_shard in legendary_items:
#             legendary_items[current_shard] += quantity
#
#         elif current_shard not in legendary_items:
#             legendary_items[current_shard] = quantity
#
#         check_for_items()
#         if shadowmourne or valanyr or dragonwrath:
#             break
#
#
# for current_shard in legendary_items:
#     print(f"{current_shard}: {legendary_items[current_shard]}")
