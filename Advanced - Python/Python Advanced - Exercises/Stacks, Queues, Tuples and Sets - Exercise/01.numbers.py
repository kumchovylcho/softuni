set_one = set(int(x) for x in input().split())
set_two = set(int(x) for x in input().split())
number_of_lines = int(input())
operations = {
    "Add First": lambda x: [set_one.add(y) for y in x],
    "Add Second": lambda x: [set_two.add(y) for y in x],
    "Remove First": lambda x: [set_one.discard(y) for y in x],
    "Remove Second": lambda x: [set_two.discard(y) for y in x],
}
for _ in range(number_of_lines):
    command_one, command_two, *info = [int(x) if x.isdigit() else x for x in input().split()]
    if command_one != "Check":
        operations[f"{command_one} {command_two}"](info)
        continue
    print(set_one.issubset(set_two) or set_two.issubset(set_one))
print(', '.join(str(x) for x in sorted(set_one)))
print(', '.join(str(x) for x in sorted(set_two)))


# first_sequence = set(int(number) for number in input().split())
# second_sequence = set(int(number) for number in input().split())
# number_of_commands = int(input())
# for _ in range(number_of_commands):
#     data = [int(item) if item.isdigit() else item for item in input().split()]
#     command = data[0] + data[1]
#     if command == 'AddFirst':
#         [first_sequence.add(digit) for digit in data[2::]]
#     elif command == 'AddSecond':
#         [second_sequence.add(digit) for digit in data[2::]]
#     elif command == 'RemoveFirst':
#         [first_sequence.discard(number) for number in data[2::]]
#     elif command == 'RemoveSecond':
#         [second_sequence.discard(number) for number in data[2::]]
#     elif command == 'CheckSubset':
#         if second_sequence.issubset(first_sequence):
#             print(True)
#         elif not second_sequence.issubset(first_sequence):
#             print(False)
# sorted_first_sequence = sorted(first_sequence)
# sorted_second_sequence = sorted(second_sequence)
# print(*sorted_first_sequence, sep=', ')
# print(*sorted_second_sequence, sep=', ')