rows, cols = [int(x) for x in input().split()]
snake = input()
snake_index = 0
for row in range(rows):
    result = []
    for col in range(cols):
        if snake_index == len(snake):
            snake_index = 0
        if row % 2 == 0:
            result.append(snake[snake_index])
        elif row % 2 != 0:
            result.insert(0, snake[snake_index])
        snake_index += 1
    print(''.join(result))
