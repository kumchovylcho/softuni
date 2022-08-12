budget_for_tereza_for_one_day = float(input())
money_that_she_wins_per_day = float(input())
money_spendings_for_whole_period = float(input())
price_of_the_gift = float(input())
pocket_money = 5 * budget_for_tereza_for_one_day
won_money = 5 * money_that_she_wins_per_day
total_saved = pocket_money + won_money
money_left = total_saved - money_spendings_for_whole_period
if money_left >= price_of_the_gift:
    print(f"Profit: {money_left:.2f} BGN, the gift has been purchased.")
else:
    diff = abs(money_left - price_of_the_gift)
    print(f"Insufficient money: {diff:.2f} BGN.")
