number_of_joinery = int(input())
type_of_joinery = input()
delivery = input()
JOI_90_130 = 110
JOI_100_150 = 140
JOI_130_180 = 190
JOI_200_300 = 250
JOI_90x130_more_than_30 = 0.05
JOI_90x130_more_than_60 = 0.08
JOI_100x150_more_than_40 = 0.06
JOI_100x150_more_than_80 = 0.10
JOI_130x180_more_than_20 = 0.07
JOI_130x180_more_than_50 = 0.12
JOI_200x300_more_than_25 = 0.09
JOI_200x300_more_than_50 = 0.14
more_than_99_after_sum = 0.04
total_price = 0
delivery_price = 60

if type_of_joinery == "90X130":
    total_price = number_of_joinery * JOI_90_130
    if 30 < number_of_joinery <= 60:
        total_price = total_price - (total_price * JOI_90x130_more_than_30)
    elif number_of_joinery > 60:
        total_price = total_price - (total_price * JOI_90x130_more_than_60)
elif type_of_joinery == "100X150":
    total_price = number_of_joinery * JOI_100_150
    if 40 < number_of_joinery <= 80:
        total_price = total_price - (total_price * JOI_100x150_more_than_40)
    elif number_of_joinery > 80:
        total_price = total_price - (total_price * JOI_100x150_more_than_80)
elif type_of_joinery == "130X180":
    total_price = number_of_joinery * JOI_130_180
    if 20 < number_of_joinery <= 50:
        total_price = total_price - (total_price * JOI_130x180_more_than_20)
    elif number_of_joinery > 50:
        total_price = total_price - (total_price * JOI_130x180_more_than_50)
elif type_of_joinery == "200X300":
    total_price = number_of_joinery * JOI_200_300
    if 25 < number_of_joinery <= 50:
        total_price = total_price - (total_price * JOI_200x300_more_than_25)
    elif number_of_joinery > 50:
        total_price = total_price - (total_price * JOI_200x300_more_than_50)
if delivery == "With delivery":
    total_price += delivery_price
else:
    total_price += 0
if number_of_joinery > 99:
    total_price = total_price - (total_price * more_than_99_after_sum)
else:
    total_price += 0
if number_of_joinery < 10:
    print("Invalid order")
else:
    print(f"{total_price:.2f} BGN")