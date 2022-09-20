group_size, package = int(input()), input()
restaurant_prices = {
    'Small Hall': {'price': 2500},
    'Terrace': {'price': 5000},
    'Great Hall': {'price': 7500},
    'Normal': {'price': 500, 'discount': 0.95},
    'Gold': {'price': 750, 'discount': 0.9},
    'Platinum': {'price': 1000, 'discount': 0.85}
}
hall_name = ''
price_per_person = 0

if 0 < group_size <= 50:
    hall_name = 'Small Hall'

elif 50 < group_size <= 100:
    hall_name = 'Terrace'

elif 100 < group_size <= 120:
    hall_name = 'Great Hall'

if len(hall_name):
    price_per_person = ((restaurant_prices[hall_name] + restaurant_prices[package]['price']) *
                        restaurant_prices[package]['discount']) / group_size
    print(f"We can offer you the {hall_name}\nThe price per person is {price_per_person:.2f}$")
else:
    print("We do not have an appropriate hall.")