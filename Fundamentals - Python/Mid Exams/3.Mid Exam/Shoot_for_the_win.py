def shoot_target(current_index):
    if 0 <= current_index < len(numbers):
        shot_value = numbers[current_index]
        numbers[current_index] = -1
        for count, item in enumerate(numbers):
            if item == -1:
                continue
            if item > shot_value:
                numbers[count] -= shot_value
            elif item <= shot_value:
                numbers[count] += shot_value


numbers = [int(x) for x in input().split()]
index = input()
while index != "End":
    index = int(index)
    shoot_target(index)
    index = input()


print(f"Shot targets: {numbers.count(-1)} -> ", end="")
print(*numbers, sep=" ")
