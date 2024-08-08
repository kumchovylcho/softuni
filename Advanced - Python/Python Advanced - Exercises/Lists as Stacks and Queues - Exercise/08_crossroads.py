from collections import deque

green_window = int(input())
free_window = int(input())
total_green_window = green_window
total_cars_passed = 0
cars_que = deque()
incident = False
END_COMMAND = "END"
GREEN_COMMAND = "green"

info = input()
while info != END_COMMAND:
    if info != GREEN_COMMAND:
        cars_que.append(info)
        info = input()
        continue

    while total_green_window > 0 and cars_que:
        car = cars_que.popleft()

        total_window = total_green_window + free_window
        car_can_pass = total_window >= len(car)
        if not car_can_pass:
            hit_at = car[total_window:total_window + 1]
            print(f"A crash happened!\n{car} was hit at {hit_at}.")
            incident = True
            break

        total_green_window -= len(car)
        total_cars_passed += 1

    if incident:
        break

    total_green_window = green_window
    info = input()

else:
    print(f"Everyone is safe.\n{total_cars_passed} total cars passed the crossroads.")