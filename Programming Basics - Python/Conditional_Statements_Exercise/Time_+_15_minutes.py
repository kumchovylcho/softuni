hours = int(input())
minutes = int(input())
total_time = (hours * 60) + minutes + 15
hour = total_time // 60
minute = total_time % 60

if hour > 23:
    hour = 0

if minute < 10:
    print(f"{hour}:0{minute}")
else:
    print(f"{hour}:{minute}")
