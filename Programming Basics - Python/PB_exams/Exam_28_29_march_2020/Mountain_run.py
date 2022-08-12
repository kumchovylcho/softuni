record = float(input())
distance = float(input())
time_for_climbing_1_meter = float(input())
extra_seconds = 0
if distance > 50:
    slowing_down = distance // 50
    extra_seconds += slowing_down * 30
time_to_climb = distance * time_for_climbing_1_meter + extra_seconds
if time_to_climb >= record:
    seconds_slower = time_to_climb - record
    print(f"No! He was {seconds_slower:.2f} seconds slower.")
else:
    print(f"Yes! The new record is {time_to_climb:.2f} seconds.")

