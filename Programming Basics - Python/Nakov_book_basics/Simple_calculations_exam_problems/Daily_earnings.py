working_days_in_month = int(input())
money_made_per_day = float(input())
dollars_to_leva_ratio = float(input())
for_one_month = working_days_in_month * money_made_per_day
bonus_for_the_year = for_one_month * 2.5
for_years = (for_one_month * 12) + bonus_for_the_year
for_years *= 0.75   # taxes
year_profit = for_years * dollars_to_leva_ratio
average_earnings_per_day = year_profit / 365
print(f"{average_earnings_per_day:.2f}")
