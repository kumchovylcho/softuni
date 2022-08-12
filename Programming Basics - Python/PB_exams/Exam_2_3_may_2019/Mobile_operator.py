term_of_contract = input()   # one or two
type_of_contract = input()   # small, middle, large, extra large
added_mobile_internet = input()  # yes or no
number_of_months_for_payment = int(input())
price = 0
if type_of_contract == "Small":
    if term_of_contract == "one":
        price = 9.98
    else:
        price = 8.58
elif type_of_contract == "Middle":
    if term_of_contract == "one":
        price = 18.99
    else:
        price = 17.09
elif type_of_contract == "Large":
    if term_of_contract == "one":
        price = 25.98
    else:
        price = 23.59
else:
    if term_of_contract == "one":
        price = 35.99
    else:
        price = 31.79
if added_mobile_internet == "yes":
    if price <= 10:
        price += 5.50
    elif 10 < price <= 30:
        price += 4.35
    elif price > 30:
        price += 3.85
total = price * number_of_months_for_payment
if term_of_contract == "two":
    total *= 0.9625
print(f"{total:.2f} lv.")
