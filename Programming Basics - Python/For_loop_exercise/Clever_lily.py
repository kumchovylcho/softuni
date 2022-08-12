lily_years_old = int(input())
price_of_washing_machine = float(input())
price_for_one_toy = int(input())
money_saved = 0
extra_money = money_saved
toys_counter = 0
brother_money_stealed = 0
for year in range(1, lily_years_old + 1):
    if year % 2 == 0:
        money_saved += 10
        extra_money += money_saved
        brother_money_stealed += 1
    else:
        toys_counter += 1
money_from_sold_toys = toys_counter * price_for_one_toy
total_saved = extra_money + money_from_sold_toys - brother_money_stealed
diff = abs(total_saved - price_of_washing_machine)
if total_saved >= price_of_washing_machine:
    print(f"Yes! {diff:.2f}")
else:
    print(f"No! {diff:.2f}")
