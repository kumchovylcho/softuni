cells = input().split("#")
water_left = int(input())
putted_out_fire_cells = []
effort = 0

for cell in cells:
    fire_type, water_needed = [int(x) if x.isdigit() else x for x in cell.split(" = ")]
    if water_left < water_needed:
        continue

    for fire, lower_range, higher_range in (("High", 81, 125), ("Medium", 51, 80), ("Low", 1, 50)):
        if fire == fire_type and lower_range <= water_needed <= higher_range:
            putted_out_fire_cells.append(water_needed)
            effort += water_needed * 0.25
            water_left -= water_needed

print("Cells:")
for cell in putted_out_fire_cells:
    print(f" - {cell}")
print(f"Effort: {effort:.2f}\nTotal Fire: {sum(putted_out_fire_cells)}")





# fire_with_cells = input().split("#")
# current_water = int(input())
# putted_out_fire_cells = []
# effort = 0
# for cell in fire_with_cells:
#     is_valid = False
#     list_with_cells = cell.split()
#     water_needed = int(list_with_cells[2])
#     if current_water >= water_needed:
#         if "High" in list_with_cells and water_needed in range(81, 126) or \
#          "Medium" in list_with_cells and water_needed in range(51, 81) or \
#          "Low" in list_with_cells and water_needed in range(1, 51):
#             is_valid = True
#     if is_valid:
#         putted_out_fire_cells.append(water_needed)
#         effort += water_needed * 0.25
#         current_water -= water_needed
#
# print("Cells:")
# for cell in putted_out_fire_cells:
#     print(f" - {cell}")
# print(f"Effort: {effort:.2f}\nTotal Fire: {sum(putted_out_fire_cells)}")
