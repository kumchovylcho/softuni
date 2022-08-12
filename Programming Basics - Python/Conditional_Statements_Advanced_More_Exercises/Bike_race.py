number_junior_bikers = int(input())
number_senior_bikers = int(input())
road = input()
junior_price = 0
senior_price = 0
if road == "trail":
    junior_price = 5.50
    senior_price = 7
elif road == "cross-country":
    junior_price = 8
    senior_price = 9.50
    if number_junior_bikers + number_senior_bikers >= 50:
        junior_price *= 0.75
        senior_price *= 0.75
elif road == "downhill":
    junior_price = 12.25
    senior_price = 13.75
else:
    junior_price = 20
    senior_price = 21.50

total = ((junior_price * number_junior_bikers) + (senior_price * number_senior_bikers)) * 0.95
print(f"{total:.2f}")
