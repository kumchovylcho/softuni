from collections import deque


def give_duck(toy_time: int, toys: dict):
    for time, value in toys.items():
        if toy_time <= time:
            value['count'] += 1
            return True

    return False


task_time = deque(int(x) for x in input().split())
number_of_tasks = [int(x) for x in input().split()]

duck_times = {
    60: {"name": "Darth Vader Ducky", "count": 0},
    120: {"name": "Thor Ducky", "count": 0},
    180: {"name": "Big Blue Rubber Ducky", "count": 0},
    240: {"name": "Small Yellow Rubber Ducky", "count": 0},
}

while task_time and number_of_tasks:
    current_time = task_time.popleft()
    current_task = number_of_tasks.pop()

    calculated_time = current_time * current_task

    if not give_duck(calculated_time, duck_times):
        task_time.append(current_time)
        number_of_tasks.append(current_task - 2)


print("Congratulations, all tasks have been completed! Rubber ducks rewarded:")

for value in duck_times.values():
    print(f"{value['name']}: {value['count']}")
