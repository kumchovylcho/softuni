days = int(input())
hours_per_day = int(input())

total = 0

for day in range(1, days + 1):
    money_spent_for_the_day = 0

    for hour in range(1, hours_per_day + 1):
        if day % 2 == 0 and hour % 2 != 0:
            money_spent_for_the_day += 2.5

        elif day % 2 != 0 and hour % 2 == 0:
            money_spent_for_the_day += 1.25

        else:
            money_spent_for_the_day += 1

    total += money_spent_for_the_day

    print(f"Day: {day} - {money_spent_for_the_day:.2f} leva")

print(f"Total: {total:.2f} leva")
