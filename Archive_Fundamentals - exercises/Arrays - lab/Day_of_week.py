day = int(input()) - 1
days_in_week = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
if 0 <= day < len(days_in_week):
    print(days_in_week[day])
else:
    print("Invalid Day!")