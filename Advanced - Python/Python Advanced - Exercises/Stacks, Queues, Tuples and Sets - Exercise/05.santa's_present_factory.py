from collections import deque

materials_for_toys = deque(int(x) for x in input().split())
magic_level = deque(int(x) for x in input().split())
crafted_items = {
    150: {'collected': 0, 'toy': 'Doll'},
    250: {'collected': 0, 'toy': 'Wooden train'},
    300: {'collected': 0, 'toy': 'Teddy bear'},
    400: {'collected': 0, 'toy': 'Bicycle'},
}
while materials_for_toys and magic_level:
    current_toy, current_magic = materials_for_toys.pop(), magic_level.popleft()
    if current_toy == 0 and current_magic == 0:
        continue
    if current_toy == 0:
        magic_level.appendleft(current_magic)
        continue
    if current_magic == 0:
        materials_for_toys.append(current_toy)
        continue
    result = current_toy * current_magic
    if result in crafted_items:
        crafted_items[result]['collected'] += 1
        continue
    if result < 0:
        materials_for_toys.append(current_toy + current_magic)
        continue
    if result > 0:
        materials_for_toys.append(current_toy + 15)
if (crafted_items[150]['collected'] and crafted_items[250]['collected']) \
        or (crafted_items[300]['collected'] and crafted_items[400]['collected']):
    print("The presents are crafted! Merry Christmas!")
else:
    print("No presents this Christmas!")
if materials_for_toys:
    print(f"Materials left: {', '.join([str(x) for x in materials_for_toys][::-1])}")
if magic_level:
    print(f"Magic left: {', '.join(str(x) for x in magic_level)}")
for points, values in sorted(crafted_items.items(), key=lambda name: name[1]['toy']):
    if values['collected']:
        print(f"{values['toy']}: {values['collected']}")


# from collections import deque
# boxes_with_materials = deque(int(material) for material in input().split())
# magic_values = deque(int(value) for value in input().split())
# prices = {
#     150: 'Doll',
#     250: 'Wooden train',
#     300: 'Teddy bear',
#     400: 'Bicycle'}
# presents = {
#     'Doll': 0,
#     'Wooden train': 0,
#     'Teddy bear': 0,
#     'Bicycle': 0
# }
# while boxes_with_materials and magic_values:
#     if boxes_with_materials[-1] == 0 or magic_values[0] == 0:
#         if boxes_with_materials[-1] == 0:
#             boxes_with_materials.pop()
#         if magic_values[0] == 0:
#             magic_values.popleft()
#         continue
#     try_craft = boxes_with_materials[-1] * magic_values[0]
#     if try_craft in prices:
#         presents[prices[try_craft]] += 1
#         boxes_with_materials.pop()
#         magic_values.popleft()
#     elif try_craft < 0:
#         negative_sum = boxes_with_materials[-1] + magic_values[0]
#         boxes_with_materials[-1] = negative_sum
#         magic_values.popleft()
#     elif try_craft > 0:
#         magic_values.popleft()
#         boxes_with_materials[-1] += 15
#
#
# if (presents['Doll'] and presents['Wooden train']) or (presents['Teddy bear'] and presents['Bicycle']):
#     print("The presents are crafted! Merry Christmas!")
# else:
#     print("No presents this Christmas!")
# if boxes_with_materials:
#     print(f"Materials left: {', '.join(list(str(x) for x in boxes_with_materials)[::-1])}")
# if magic_values:
#     print(f"Magic left: {', '.join(str(x) for x in magic_values)}")
# for key, value in sorted(presents.items()):
#     if value:
#         print(f"{key}: {value}")