from math import ceil
name_of_serie = input()
lenght_of_episode = int(input())
lenght_of_break = int(input())
eating_time = lenght_of_break / 8
resting_time = lenght_of_break / 4
total_time_to_rest = eating_time + resting_time
free_time_to_watch = lenght_of_break - total_time_to_rest
if free_time_to_watch >= lenght_of_episode:
    diff = ceil(free_time_to_watch - lenght_of_episode)
    print(f"You have enough time to watch {name_of_serie} and left with {diff} minutes free time.")
else:
    diff = ceil(lenght_of_episode - free_time_to_watch)
    print(f"You don't have enough time to watch {name_of_serie}, you need {diff} more minutes.")
