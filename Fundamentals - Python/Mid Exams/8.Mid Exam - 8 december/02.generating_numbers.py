numbers = [int(x) for x in input().split()]
command = input()
while command != "END":
    task, *info = [int(x) if x[-1].isdigit() else x for x in command.split()]
    if task == "add":
        numbers = info[2:] + numbers
    elif task == "remove" and info[0] == "greater":
        value = info[-1]
        numbers = [x for x in numbers if value > x]
    elif task == "replace":
        value, replacement = info
        if value in numbers:
            index = numbers.index(value)
            numbers[index] = replacement
    elif task == "remove":
        index = info[-1]
        if 0 <= index < len(numbers):
            numbers.pop(index)
    elif task == "find" and info[0] == "even":
        print(' '.join(str(x) for x in numbers if x % 2 == 0))
    elif task == "find":
        print(' '.join(str(x) for x in numbers if x % 2 != 0))
    command = input()
print(*numbers, sep=', ')