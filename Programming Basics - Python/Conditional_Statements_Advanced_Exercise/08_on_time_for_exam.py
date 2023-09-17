hour_exam = int(input())
minute_exam = int(input())

hour_arrival = int(input())
minute_arrival = int(input())

total_min_exam = hour_exam * 60 + minute_exam
total_min_arrival = hour_arrival * 60 + minute_arrival

diff = abs(total_min_exam - total_min_arrival)

hrs = diff // 60
mins = diff % 60

status = ""
when = "before the start"
time = f"{hrs}:{mins:02d} hours"

if 0 <= total_min_exam - total_min_arrival <= 30:
    status = "On time"

elif total_min_arrival < total_min_exam:
    status = "Early"

elif total_min_arrival > total_min_exam:
    status = "Late"
    when = "after the start"


if diff < 60:
    time = f"{diff} minutes"

print(status)
if diff:
    result = f"{time} {when}"
    print(result)

#########################################################################

# exam_hour = int(input())
# exam_minute = int(input())
# arrival_hour = int(input())
# arrival_minute = int(input())
# total_minutes_exam = (exam_hour * 60) + exam_minute
# total_minutes_arrival = (arrival_hour * 60) + arrival_minute
#
# diff = abs(total_minutes_exam - total_minutes_arrival)
# if total_minutes_arrival > total_minutes_exam:
#     if diff < 60:
#         print(f"Late\n{diff} minutes after the start")
#     else:
#         hour = diff // 60
#         minutes = diff % 60
#         if minutes < 10:
#             print(f"Late\n{hour}:0{minutes} hours after the start")
#         else:
#             print(f"Late\n{hour}:{minutes} hours after the start")
#
# elif total_minutes_exam == total_minutes_arrival or diff <= 30:
#     print("On time")
#     if 1 <= diff <= 30:
#         print(f"{diff} minutes before the start")
# else:
#     if diff < 60:
#         print(f"Early\n{diff} minutes before the start")
#     else:
#         hour = diff // 60
#         minutes = diff % 60
#         if minutes < 10:
#             print(f"Early\n{hour}:0{minutes} hours before the start")
#         else:
#             print(f"Early\n{hour}:{minutes} hours before the start")
