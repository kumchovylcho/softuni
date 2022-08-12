rest_days = int(input())
norm_for_the_year = 30000
while_working = (365 - rest_days) * 63
while_resting = rest_days * 127
total_playtime = while_working + while_resting
difference = abs(norm_for_the_year - total_playtime)
hours = difference // 60
minutes = difference % 60
if total_playtime >= norm_for_the_year:
    print(f"Tom will run away")
    print(f"{hours} hours and {minutes} minutes more for play")
else:
    print(f"Tom sleeps well")
    print(f"{hours} hours and {minutes} minutes less for play")