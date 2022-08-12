number_of_days = int(input())
number_of_hours_for_every_day = int(input())
total_money = 0
daily_money = 0
for day in range(1, number_of_days + 1):
    total_money += daily_money
    daily_money = 0
    for hour in range(1, number_of_hours_for_every_day + 1):
        if day % 2 == 0 and hour % 2 != 0:
            daily_money += 2.50
        elif day % 2 != 0 and hour % 2 == 0:
            daily_money += 1.25
        else:
            daily_money += 1
    print(f"Day: {day} - {daily_money:.2f} leva")
total_money += daily_money
print(f"Total: {total_money:.2f} leva")
