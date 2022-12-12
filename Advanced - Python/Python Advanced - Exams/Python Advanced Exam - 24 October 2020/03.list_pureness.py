from collections import deque


def best_list_pureness(numbers, rotations):
    numbers = deque(numbers)
    maximum_possible_result = 0
    best_rotation = 0
    for rotation in range(rotations + 1):
        current_result = 0
        for index, number in enumerate(numbers):
            current_result += index * number
        if current_result > maximum_possible_result:
            maximum_possible_result = current_result
            best_rotation = rotation
        numbers.rotate(1)
    return f"Best pureness {maximum_possible_result} after {best_rotation} rotations"


test = ([1, 2, 3, 4, 5], 10)
result = best_list_pureness(*test)
print(result)