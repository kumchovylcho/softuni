from collections import deque
water_in_dispenser = int(input())
que_of_people_for_water = deque()
name = input()
while name != "Start":
    que_of_people_for_water.append(name)
    name = input()
command = input()
while command != "End":
    if command.isdigit():
        liters_of_water = int(command)
        if water_in_dispenser >= liters_of_water:
            print(f"{que_of_people_for_water.popleft()} got water")
            water_in_dispenser -= liters_of_water
        elif water_in_dispenser < liters_of_water:
            print(f"{que_of_people_for_water.popleft()} must wait")
    elif not command.isdigit():
        _, liters_refill = [int(item) if item.isdigit() else item for item in command.split()]
        water_in_dispenser += liters_refill
    command = input()
print(f"{water_in_dispenser} liters left")