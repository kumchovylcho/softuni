numbers = int(input())
by_2 = 0
by_3 = 0
by_4 = 0
for number in range(1, numbers + 1):
    current_number = int(input())
    if current_number % 2 == 0:
        by_2 += 1
    if current_number % 3 == 0:
        by_3 += 1
    if current_number % 4 == 0:
        by_4 += 1
percentage_by_2 = by_2 / numbers * 100
percentage_by_3 = by_3 / numbers * 100
percentage_by_4 = by_4 / numbers * 100
print(f"{percentage_by_2:.2f}%\n{percentage_by_3:.2f}%\n{percentage_by_4:.2f}%")
