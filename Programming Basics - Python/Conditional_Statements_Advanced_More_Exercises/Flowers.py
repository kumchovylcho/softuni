number_of_purchased_chrysanthemums = int(input())
number_of_purchased_roses = int(input())
number_of_purchased_tulips = int(input())
season = input()
holiday = input()
price_chrysanthemums = 0
price_roses = 0
price_tulips = 0
if season == "Spring" or season == "Summer":
    price_chrysanthemums = 2.00
    price_roses = 4.10
    price_tulips = 2.50
    if holiday == "Y":
        price_chrysanthemums *= 1.15
        price_roses *= 1.15
        price_tulips *= 1.15
else:
    price_chrysanthemums = 3.75
    price_roses = 4.50
    price_tulips = 4.15
    if holiday == "Y":
        price_chrysanthemums *= 1.15
        price_roses *= 1.15
        price_tulips *= 1.15
total = (number_of_purchased_chrysanthemums * price_chrysanthemums) + (number_of_purchased_roses * price_roses) + (number_of_purchased_tulips * price_tulips)
if season == "Spring":
    if number_of_purchased_tulips > 7:
        total *= 0.95
if season == "Winter":
    if number_of_purchased_roses >= 10:
        total *= 0.90
if number_of_purchased_roses + number_of_purchased_tulips + number_of_purchased_chrysanthemums > 20:
    total *= 0.80
print(f"{total + 2:.2f}")
