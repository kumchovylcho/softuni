from math import floor
record = float(input())
distance_meters = float(input())
time_swim_one_meter = float(input())
water_slow_down_seconds = 12.5
seconds_swim = distance_meters * time_swim_one_meter
times_slow_down = floor(distance_meters // 15)
extra_seconds = times_slow_down * water_slow_down_seconds
total_time = extra_seconds + seconds_swim
if total_time < record:
    print(f"Yes, he succeeded! The new world record is {total_time:.2f} seconds.")
else:
    diff = total_time - record
    print(f"No, he failed! He was {diff:.2f} seconds slower.")