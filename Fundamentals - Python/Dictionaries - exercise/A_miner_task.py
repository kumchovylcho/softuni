mined_materials = dict()

material = input()
while material != "stop":
    quantity = int(input())

    if material not in mined_materials:
        mined_materials[material] = quantity

    elif material in mined_materials:
        mined_materials[material] += quantity

    material = input()

for key in mined_materials:
    print(f"{key} -> {mined_materials[key]}")

# miner_resources = dict()
#
# minerals = input()
# while minerals != "stop":
#     quantity = int(input())
#
#     if minerals in miner_resources:
#         miner_resources[minerals] += quantity
#     elif minerals not in miner_resources:
#         miner_resources[minerals] = quantity
#
#     minerals = input()
#
# [print(f"{mineral} -> {miner_resources[mineral]}") for mineral in miner_resources]
