length = float(input()) * 100
width = float(input()) * 100
width -= 100  # for corridor
working_desks_for_rows = length // 120
working_desks_for_col = width // 70
all_desks = (working_desks_for_rows * working_desks_for_col) - 3
print(int(all_desks))