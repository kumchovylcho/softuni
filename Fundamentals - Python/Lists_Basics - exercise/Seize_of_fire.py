fire_with_cells = input().split("#")
current_water = int(input())
putted_out_fire_cells = []
effort = 0
for cell in fire_with_cells:
    is_valid = False
    list_with_cells = (cell.split())
    if current_water >= int(list_with_cells[2]):
        if "High" in list_with_cells and int(list_with_cells[2]) in range(81, 126):
            is_valid = True
        elif "Medium" in list_with_cells and int(list_with_cells[2]) in range(51, 81):
            is_valid = True
        elif "Low" in list_with_cells and int(list_with_cells[2]) in range(1, 51):
            is_valid = True
    if is_valid:
        putted_out_fire_cells.append(int(list_with_cells[2]))
        effort += int(list_with_cells[2]) * 0.25
        current_water -= int(list_with_cells[2])

print("Cells:")
for cell in putted_out_fire_cells:
    print(f" - {cell}")
print(f"Effort: {effort:.2f}\nTotal Fire: {sum(putted_out_fire_cells)}")
