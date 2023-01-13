from collections import deque

number_pumps = int(input())

circle = deque()
for _ in range(number_pumps):
    amount_petrol, distance = [int(x) for x in input().split()]
    circle.append((amount_petrol, distance))

for i in range(len(circle)):
    current_circle = circle.copy()
    saved_petrol = 0
    while current_circle:
        drive = current_circle.popleft()
        if drive[0] + saved_petrol >= drive[1]:
            saved_petrol += drive[0] - drive[1]
        else:
            break
    if len(current_circle) == 0:
        print(i)
        break
    circle.rotate(-1)


# from collections import deque
# queue = deque()
# pumps = int(input())
# for _ in range(pumps):
#     gas_pump = input().split()
#     queue.append([int(gas_pump[0]), int(gas_pump[1])])
#
# for attempt in range(pumps):
#     fuel_tank = 0
#     pumps_travelled = 0
#     for gas_pump in queue:
#         fuel, distance_to_next_pump = gas_pump[0], gas_pump[1]
#         fuel_tank += fuel
#         if fuel_tank < distance_to_next_pump:
#             break
#         fuel_tank -= distance_to_next_pump
#         pumps_travelled += 1
#     if pumps_travelled == len(queue):
#         print(attempt)
#         break
#
#     queue.rotate(-1)


