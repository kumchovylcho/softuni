budget = float(input())
litres_fuel_needed = float(input())
day_of_week = input()   # saturday or sunday

total = 2.10 * litres_fuel_needed + 100
if day_of_week == "Saturday":
    total *= 0.9
else:
    total *= 0.8
diff = abs(budget - total)
if total <= budget:
    print(f"Safari time! Money left: {diff:.2f} lv.")
else:
    print(f"Not enough money! Money needed: {diff:.2f} lv.")
