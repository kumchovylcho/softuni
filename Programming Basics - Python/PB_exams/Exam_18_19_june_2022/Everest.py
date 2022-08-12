current_climbing_meters = 5364
days_of_climbing = 1
is_reached = False
is_sleeping = input()
while is_sleeping != "END":
    climbed_meters = int(input())
    if is_sleeping == "Yes":
        days_of_climbing += 1
    current_climbing_meters += climbed_meters
    if current_climbing_meters >= 8848:
        is_reached = True
        break
    if days_of_climbing == 5:
        break
    is_sleeping = input()
if is_reached:
    print(f"Goal reached for {days_of_climbing} days!")
else:
    print(f"Failed!\n{current_climbing_meters}")
