car_time_numbers = [int(number) for number in input().split()]

middle_of_the_list = len(car_time_numbers) // 2

left_car_timer = 0
right_car_timer = 0

for left_car in range(middle_of_the_list):
    if car_time_numbers[left_car] == 0:
        left_car_timer *= 0.8
    elif car_time_numbers[left_car] != 0:
        left_car_timer += car_time_numbers[left_car]

for right_car in range(len(car_time_numbers) - 1, middle_of_the_list, -1):
    if car_time_numbers[right_car] == 0:
        right_car_timer *= 0.8
    elif car_time_numbers[right_car] != 0:
        right_car_timer += car_time_numbers[right_car]

if left_car_timer > right_car_timer:
    print(f"The winner is right with total time: {right_car_timer:.1f}")
elif right_car_timer > left_car_timer:
    print(f"The winner is left with total time: {left_car_timer:.1f}")
