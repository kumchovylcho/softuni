day_of_week = input()
if day_of_week == "Monday" \
    or day_of_week == "Tuesday" \
    or day_of_week == "Friday":
    price = 12
elif day_of_week == "Thursday" \
    or day_of_week == "Wednesday":
    price = 14
else:
    price = 16
print(price)
