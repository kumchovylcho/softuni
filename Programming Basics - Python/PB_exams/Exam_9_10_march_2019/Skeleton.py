
minutes_of_control = int(input())
seconds_of_control = int(input())
lenght_of_beehive = float(input())
seconds_for_passing_100_meters = int(input())
control_seconds = minutes_of_control * 60 + seconds_of_control
times_getting_slowed = lenght_of_beehive / 120
extra_seconds = times_getting_slowed * 2.5
marin_time = (lenght_of_beehive / 100) * seconds_for_passing_100_meters - extra_seconds
diff = abs(marin_time - control_seconds)
if marin_time <= control_seconds:
    print(f"Marin Bangiev won an Olympic quota!\nHis time is {marin_time:.3f}.")
else:
    print(f"No, Marin failed! He was {diff:.3f} second slower.")
