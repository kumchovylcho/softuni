hour = int(input())
minutes = int(input())
if hour < 23:
    if minutes + 15 > 59:
        hour += 1
        minutes += 15
        minutes -= 60
    else:
        minutes += 15
elif hour == 23:
    if minutes + 15 > 59:
        hour = 0
        minutes += 15
        minutes -= 60
    else:
        minutes += 15
if minutes < 10:
    print(f"{hour}:0{minutes}")
else:
    print(f"{hour}:{minutes}")
