day_of_week = input()
if day_of_week == "Monday" \
    or day_of_week == "Tuesday" \
    or day_of_week == "Wednesday" \
    or day_of_week == "Thursday" \
    or day_of_week == "Friday":
    print("Working day")
elif day_of_week == "Saturday" \
    or day_of_week == "Sunday":
    print("Weekend")
else:
    print("Error")
