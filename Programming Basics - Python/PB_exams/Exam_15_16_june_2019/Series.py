budget = float(input())
number_of_series = int(input())
budget_left = budget
for series in range(1, number_of_series + 1):
    name_of_series = input()
    price_for_series = float(input())
    if name_of_series == "Thrones":
        budget_left -= price_for_series * 0.5
    elif name_of_series == "Lucifer":
        budget_left -= price_for_series * 0.6
    elif name_of_series == "Protector":
        budget_left -= price_for_series * 0.7
    elif name_of_series == "TotalDrama":
        budget_left -= price_for_series * 0.8
    elif name_of_series == "Area":
        budget_left -= price_for_series * 0.9
    else:
        budget_left -= price_for_series
if budget_left < 0:
    print(f"You need {abs(budget_left):.2f} lv. more to buy the series!")
else:
    print(f"You bought all the series and left with {budget_left:.2f} lv.")
