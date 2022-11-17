from collections import deque
boxes_with_materials = deque(int(material) for material in input().split())
magic_values = deque(int(value) for value in input().split())
prices = {
    150: 'Doll',
    250: 'Wooden train',
    300: 'Teddy bear',
    400: 'Bicycle'}
presents = {
    'Doll': 0,
    'Wooden train': 0,
    'Teddy bear': 0,
    'Bicycle': 0
}
while boxes_with_materials and magic_values:
    if boxes_with_materials[-1] == 0 or magic_values[0] == 0:
        if boxes_with_materials[-1] == 0:
            boxes_with_materials.pop()
        if magic_values[0] == 0:
            magic_values.popleft()
        continue
    try_craft = boxes_with_materials[-1] * magic_values[0]
    if try_craft in prices:
        presents[prices[try_craft]] += 1
        boxes_with_materials.pop()
        magic_values.popleft()
    elif try_craft < 0:
        negative_sum = boxes_with_materials[-1] + magic_values[0]
        boxes_with_materials[-1] = negative_sum
        magic_values.popleft()
    elif try_craft > 0:
        magic_values.popleft()
        boxes_with_materials[-1] += 15


if (presents['Doll'] and presents['Wooden train']) or (presents['Teddy bear'] and presents['Bicycle']):
    print("The presents are crafted! Merry Christmas!")
else:
    print("No presents this Christmas!")
if boxes_with_materials:
    print(f"Materials left: {', '.join(list(str(x) for x in boxes_with_materials)[::-1])}")
if magic_values:
    print(f"Magic left: {', '.join(str(x) for x in magic_values)}")
for key, value in sorted(presents.items()):
    if value:
        print(f"{key}: {value}")