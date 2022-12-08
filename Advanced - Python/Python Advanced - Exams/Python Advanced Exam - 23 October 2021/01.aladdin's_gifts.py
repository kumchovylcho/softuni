from collections import deque


def try_to_craft(current_value):
    for material, value in items.items():
        if value['lower'] <= current_value <= value['upper']:
            items[material]['count'] += 1
            return


def check_for_crafted_pairs():
    if items['Gemstone']['count'] > 0 and items['Porcelain Sculpture']['count'] > 0:
        return True
    elif items['Gold']['count'] > 0 and items['Diamond Jewellery']['count'] > 0:
        return True


items = {
    'Gemstone': {'lower': 100, 'upper': 199, 'count': 0},
    'Porcelain Sculpture': {'lower': 200, 'upper': 299, 'count': 0},
    'Gold': {'lower': 300, 'upper': 399, 'count': 0},
    'Diamond Jewellery': {'lower': 400, 'upper': 499, 'count': 0}
}
materials = deque(int(x) for x in input().split())
magic = deque(int(x) for x in input().split())
while materials and magic:
    current_material = materials.pop()
    current_magic = magic.popleft()
    total_magic = current_material + current_magic
    if 100 <= total_magic <= 499:
        try_to_craft(total_magic)
        continue
    if total_magic < 100 and total_magic % 2 == 0:
        current_material *= 2
        current_magic *= 3
        total_magic = current_material + current_magic
        try_to_craft(total_magic)
    elif total_magic < 100 and total_magic % 2 != 0:
        current_material *= 2
        current_magic *= 2
        total_magic = current_material + current_magic
        try_to_craft(total_magic)
    elif total_magic > 499:
        total_magic /= 2
        try_to_craft(total_magic)
if check_for_crafted_pairs():
    print("The wedding presents are made!")
else:
    print("Aladdin does not have enough wedding presents.")
if materials:
    print(f"Materials left: {', '.join(str(x) for x in materials)}")
if magic:
    print(f"Magic left: {', '.join(str(x) for x in magic)}")
for material, value in sorted(items.items()):
    if value['count'] > 0:
        print(f"{material}: {value['count']}")
