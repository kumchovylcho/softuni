descending_number, ascending_number, boundary_number = int(input()), int(input()), int(input())
combinations = 0
total_sum = 0

for digit_down in range(descending_number, 0, -1):
    for digit_up in range(1, ascending_number + 1):
        combinations += 1
        total_sum += (digit_down * digit_up) * 3
        if total_sum >= boundary_number:
            break
    if total_sum >= boundary_number:
        break

if total_sum >= boundary_number:
    print(f"{combinations} combinations\nSum: {total_sum} >= {boundary_number}")
else:
    print(f"{combinations} combinations\nSum: {total_sum}")

