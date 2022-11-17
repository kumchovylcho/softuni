first_sequence = set(int(number) for number in input().split())
second_sequence = set(int(number) for number in input().split())
number_of_commands = int(input())
for _ in range(number_of_commands):
    data = [int(item) if item.isdigit() else item for item in input().split()]
    command = data[0] + data[1]
    if command == 'AddFirst':
        [first_sequence.add(digit) for digit in data[2::]]
    elif command == 'AddSecond':
        [second_sequence.add(digit) for digit in data[2::]]
    elif command == 'RemoveFirst':
        [first_sequence.discard(number) for number in data[2::]]
    elif command == 'RemoveSecond':
        [second_sequence.discard(number) for number in data[2::]]
    elif command == 'CheckSubset':
        if second_sequence.issubset(first_sequence):
            print(True)
        elif not second_sequence.issubset(first_sequence):
            print(False)
sorted_first_sequence = sorted(first_sequence)
sorted_second_sequence = sorted(second_sequence)
print(*sorted_first_sequence, sep=', ')
print(*sorted_second_sequence, sep=', ')