total_profit = 0
visited_cities = int(input())
for city in range(1, visited_cities + 1):
    city_name, earned_money, expenses = input(), float(input()), float(input())
    if city % 5 == 0:
        earned_money *= 0.9
    if city % 3 == 0 and city % 5 != 0:
        expenses *= 1.5
    current_tour_income = earned_money - expenses
    total_profit += current_tour_income
    print(f"In {city_name} Burger Bus earned {current_tour_income:.2f} leva.")
print(f"Burger Bus total profit: {total_profit:.2f} leva.")
