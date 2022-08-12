price_of_bag_more_than_20kg = float(input())
kgs_of_bag = float(input())
days_untill_trip = int(input())
number_of_bags = int(input())
if kgs_of_bag < 10:
    price_of_bag_more_than_20kg = price_of_bag_more_than_20kg * 0.2
elif 10 <= kgs_of_bag <= 20:
    price_of_bag_more_than_20kg = price_of_bag_more_than_20kg * 0.5
elif kgs_of_bag > 20:
    price_of_bag_more_than_20kg = price_of_bag_more_than_20kg
if days_untill_trip < 7:
    price_of_bag_more_than_20kg = price_of_bag_more_than_20kg + (price_of_bag_more_than_20kg * 0.4)
elif 7 <= days_untill_trip <= 30:
    price_of_bag_more_than_20kg = price_of_bag_more_than_20kg + (price_of_bag_more_than_20kg * 0.15)
elif days_untill_trip > 30:
    price_of_bag_more_than_20kg = price_of_bag_more_than_20kg + (price_of_bag_more_than_20kg * 0.10)
total = price_of_bag_more_than_20kg * number_of_bags
print(f"The total price of bags is: {total:.2f} lv.")
