month_of_the_year = input()
number_of_nights = int(input())
price_studio = 0
price_apartment = 0
if month_of_the_year == "May" or month_of_the_year == "October":
    price_studio = 50 * number_of_nights
    price_apartment = 65 * number_of_nights
    if 8 <= number_of_nights <= 14:
        price_studio *= 0.95
    elif number_of_nights > 14:
        price_studio *= 0.70
        price_apartment *= 0.90
elif month_of_the_year == "June" or month_of_the_year == "September":
    price_studio = 75.20 * number_of_nights
    price_apartment = 68.70 * number_of_nights
    if number_of_nights > 14:
        price_studio *= 0.80
        price_apartment *= 0.90
elif month_of_the_year == "July" or month_of_the_year == "August":
    price_studio = 76 * number_of_nights
    price_apartment = 77 * number_of_nights
    if number_of_nights > 14:
        price_apartment *= 0.90
print(f"Apartment: {price_apartment:.2f} lv.\nStudio: {price_studio:.2f} lv.")
