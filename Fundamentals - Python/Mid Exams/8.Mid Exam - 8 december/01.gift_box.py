sides = 6
size_of_side = float(input())
number_of_sheets = int(input())
total_sum = 0
size_of_area = size_of_side ** 2 * sides
for sheet in range(1, number_of_sheets + 1):
    length_of_sheet = float(input())
    width_of_sheet = float(input())
    area_cover = length_of_sheet * width_of_sheet
    if sheet % 3 == 0:
        area_cover = (length_of_sheet * width_of_sheet) * 0.75
    if sheet % 5 == 0:
        area_cover = 0
    total_sum += area_cover
if total_sum >= size_of_area:
    total_area_covered = ((total_sum - size_of_area) / total_sum) * 100
    print(f"You've covered the gift box!")
    print(f"{total_area_covered:.2f}% wrap paper left.")
elif total_sum < size_of_area:
    print(f"You are out of paper!")
    total_area_covered = (total_sum / size_of_area) * 100
    print(f"{100 - total_area_covered:.2f}% of the box is not covered.")

