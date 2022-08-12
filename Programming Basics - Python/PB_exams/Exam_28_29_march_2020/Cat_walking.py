minutes_of_walking_per_day = int(input())
number_of_walks_daily = int(input())
consumed_calories_of_cat_daily = int(input())
calories_burned_per_minute = 5
total_time_for_walk = minutes_of_walking_per_day * number_of_walks_daily
total_burned_calories_daily = total_time_for_walk * calories_burned_per_minute
fifty_percent_needed = consumed_calories_of_cat_daily / 2
if total_burned_calories_daily >= fifty_percent_needed:
    print(f"Yes, the walk for your cat is enough. Burned calories per day: {total_burned_calories_daily}.")
else:
    if total_burned_calories_daily < fifty_percent_needed:
        print(f"No, the walk for your cat is not enough. Burned calories per day: {total_burned_calories_daily}.")