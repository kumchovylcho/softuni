import re
pattern = re.compile(r'([\\|#])(?P<product>[A-Za-z ]+)\1(?P<date>\d{2}/\d{2}/\d{2})\1(?P<calories>\d+)\1')
products = input()
matches = pattern.finditer(products)
products = []
calories = 0
for match in matches:
    products.append(f"Item: {match['product']}, Best before: {match['date']}, Nutrition: {match['calories']}")
    calories += int(match['calories'])
calories_consumed_per_day = 2000
food_for_n_days = calories // calories_consumed_per_day
print(f"You have food to last you for: {food_for_n_days} days!")
[print(item) for item in products]
