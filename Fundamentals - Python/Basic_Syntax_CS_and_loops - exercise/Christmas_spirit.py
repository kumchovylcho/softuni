quantity_of_products = int(input())
days_left_until_christmas = int(input())
spirit_points = 0
money_spend = 0
days_counter = 0
for day in range(days_left_until_christmas, 0, -1):
    days_counter += 1
    if days_counter % 11 == 0:
        quantity_of_products += 2
    if days_counter % 2 == 0:
        money_spend += quantity_of_products * 2
        spirit_points += 5
    if days_counter % 3 == 0:
        money_spend += (quantity_of_products * 5) + (quantity_of_products * 3)
        spirit_points += 3 + 10
    if days_counter % 5 == 0:
        money_spend += quantity_of_products * 15
        spirit_points += 17
        if days_counter % 3 == 0:
            spirit_points += 30
    if days_counter % 10 == 0:
        spirit_points -= 20
        money_spend += 5 + 3 + 15
if days_counter % 10 == 0:
    spirit_points -= 30
print(f"Total cost: {money_spend}\nTotal spirit: {spirit_points}")
