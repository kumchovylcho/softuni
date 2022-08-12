sea_vacation_num = int(input())
mountain_vacation_num = int(input())
command = input()
remaining_sea_vacations = sea_vacation_num
remaining_mountain_vacations = mountain_vacation_num
profit_sea = 0
profit_mountain = 0
while command != "Stop":
    if command == "sea":
        if remaining_sea_vacations < 1:
            command = input()
            continue
        else:
            remaining_sea_vacations -= 1
            profit_sea += 680
    if command == "mountain":
        if remaining_mountain_vacations < 1:
            command = input()
            continue
        else:
            remaining_mountain_vacations -= 1
            profit_mountain += 499
    if remaining_mountain_vacations == 0 and remaining_sea_vacations == 0:
        break
    command = input()
total_profit = profit_sea + profit_mountain
if remaining_sea_vacations == 0 and remaining_mountain_vacations == 0:
    print("Good job! Everything is sold.")
    print(f"Profit: {total_profit} leva.")
else:
    print(f"Profit: {total_profit} leva.")
