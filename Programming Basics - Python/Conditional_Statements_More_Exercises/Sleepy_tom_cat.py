number_of_rest_days = int(input())
work_days = 365 - number_of_rest_days
normative = 30000
work_day_time_for_cat = 63
rest_day_time_for_cat = 127
total_minutes_for_playtime = (number_of_rest_days * rest_day_time_for_cat) + (work_days * work_day_time_for_cat)
free_time = abs(normative - total_minutes_for_playtime)
hour = free_time // 60
minutes = free_time % 60
if total_minutes_for_playtime >= normative:
    print(f"Tom will run away\n{hour} hours and {minutes} minutes more for play")
else:
    print(f"Tom sleeps well\n{hour} hours and {minutes} minutes less for play")

