inherited_money = float(input())
year_living = int(input())

age = 18
cost_per_even_year = 12_000

for year in range(1800, year_living + 1):
    cost_for_current_year = cost_per_even_year

    if year % 2 == 1:
        cost_for_current_year = cost_per_even_year + (50 * age)

    age += 1
    inherited_money -= cost_for_current_year

if inherited_money >= 0:
    print(f'Yes! He will live a carefree life and will have {inherited_money:.2f} dollars left.')
else:
    print(f'He will need {abs(inherited_money):.2f} dollars to survive.')



################################################################################################


# money_left = float(input())
# year_to_live = int(input())
# current_money = money_left
# years_old = 18
# for year in range(1800, year_to_live + 1):
#     if year % 2 == 0:
#         current_money -= 12000
#     else:
#         current_money -= 12000 + 50 * years_old
#     years_old += 1
# if current_money >= 0:
#     print(f"Yes! He will live a carefree life and will have {current_money:.2f} dollars left.")
# else:
#     print(f"He will need {abs(current_money):.2f} dollars to survive.")
