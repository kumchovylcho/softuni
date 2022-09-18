hours = int(input())
minutes = int(input())

if hours == 23:
    if minutes > 30:
        hours = 0
        minutes -= 30
    else:
        minutes += 30
else:
    if minutes > 30:
        hours += 1
        minutes -= 30
    else:
        minutes += 30
print(f"{hours}:{minutes:02d}")
