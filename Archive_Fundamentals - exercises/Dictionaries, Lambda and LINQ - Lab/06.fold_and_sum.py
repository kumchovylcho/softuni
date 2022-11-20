from collections import deque
numbers = [int(x) for x in input().split()]
outside = (len(numbers) // 2) // 2
left_and_right = deque(numbers[:outside][::-1] + numbers[-outside:][::-1])
middle_numbers = deque(numbers[outside:-outside])
while middle_numbers and left_and_right:
    result = left_and_right.popleft() + middle_numbers.popleft()
    print(result, end=' ')