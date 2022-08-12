destination = input()
date_of_reservation = input()
number_of_nights = int(input())
prices = {"France": {
    "21-23": 30,
    "24-27": 35,
    "28-31": 40},
    "Italy": {
        "21-23": 28,
        "24-27": 32,
        "28-31": 39},
    "Germany": {
    "21-23": 32,
    "24-27": 37,
    "28-31": 43}
}
total_price = 0
if destination == "France" and date_of_reservation in prices["France"]:
    total_price = prices["France"][date_of_reservation] * number_of_nights
elif destination == "Italy" and date_of_reservation in prices["Italy"]:
    total_price = prices["Italy"][date_of_reservation] * number_of_nights
elif destination == "Germany" and date_of_reservation in prices["Germany"]:
    total_price = prices["Germany"][date_of_reservation] * number_of_nights
print(f"Easter trip to {destination} : {total_price:.2f} leva.")
