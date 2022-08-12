number_of_kilometers = int(input())
day_or_night = input()
taxi_start_price = 0.70
taxi_day_price = 0.79
taxi_night_price = 0.90
autobus = 0.09
train = 0.06
total_price = 0
if number_of_kilometers < 20 and day_or_night == "day":
    total_price += taxi_day_price * number_of_kilometers + taxi_start_price
elif number_of_kilometers < 20 and day_or_night == "night":
    total_price += taxi_night_price * number_of_kilometers + taxi_start_price
elif number_of_kilometers < 100:
    total_price += autobus * number_of_kilometers
else:
    total_price += train * number_of_kilometers
print(f"{total_price:.2f}")
