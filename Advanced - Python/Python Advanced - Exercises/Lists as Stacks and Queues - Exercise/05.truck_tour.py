from collections import deque
queue = deque()
pumps = int(input())
for _ in range(pumps):
    gas_pump = input().split()
    queue.append([int(gas_pump[0]), int(gas_pump[1])])

for attempt in range(pumps):
    fuel_tank = 0
    pumps_travelled = 0
    for gas_pump in queue:
        fuel, distance_to_next_pump = gas_pump[0], gas_pump[1]
        fuel_tank += fuel
        if fuel_tank < distance_to_next_pump:
            break
        fuel_tank -= distance_to_next_pump
        pumps_travelled += 1
    if pumps_travelled == len(queue):
        print(attempt)
        break

    queue.rotate(-1)


