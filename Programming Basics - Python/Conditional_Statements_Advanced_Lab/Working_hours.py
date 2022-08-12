time = int(input())
day_of_week = input()
if 10 <= time <= 18:
    if day_of_week == "Sunday":
        print("closed")
    else:
        print("open")
else:
    print("closed")
