month, nights_staying = input(), int(input())
studio_price, double_price, suite_price = 0, 0, 0

if month == "May" or month == "October":
    studio_price, double_price, suite_price = 50, 65, 75
    if nights_staying > 7:
        studio_price *= 0.95
elif month == "June" or month == "September":
    studio_price, double_price, suite_price = 60, 72, 82
    if nights_staying > 14:
        double_price *= 0.9
elif month == "July" or month == "August" or month == "December":
    studio_price, double_price, suite_price = 68, 77, 89
    if nights_staying > 14:
        suite_price *= 0.85

total_studio = studio_price * nights_staying
total_double = double_price * nights_staying
total_suite = suite_price * nights_staying

if (month == "October" or month == "September") and nights_staying > 7:
    total_studio -= studio_price

print(f"Studio: {total_studio:.2f} lv.")
print(f"Double: {total_double:.2f} lv.")
print(f"Suite: {total_suite:.2f} lv.")


# month, nights_staying = input(), int(input())
# studio_price, double_price, suite_price = 0, 0, 0
#
# if month == "May" or month == "October":
#     studio_price, double_price, suite_price = 50, 65, 75
#
# elif month == "June" or month == "September":
#     studio_price, double_price, suite_price = 60, 72, 82
#
# elif month == "July" or month == "August" or month == "December":
#     studio_price, double_price, suite_price = 68, 77, 89
#
# if (month == "May" or month == "October") and nights_staying > 7:
#     studio_price *= 0.95
# elif (month == "June" or month == "September") and nights_staying > 14:
#     double_price *= 0.9
# elif (month == "July" or month == "August" or month == "December") and nights_staying > 14:
#     suite_price *= 0.85
#
# total_studio = studio_price * nights_staying
# total_double = double_price * nights_staying
# total_suite = suite_price * nights_staying
#
# if (month == "October" or month == "September") and nights_staying > 7:
#     total_studio -= studio_price
#
# print(f"Studio: {total_studio:.2f} lv.")
# print(f"Double: {total_double:.2f} lv.")
# print(f"Suite: {total_suite:.2f} lv.")