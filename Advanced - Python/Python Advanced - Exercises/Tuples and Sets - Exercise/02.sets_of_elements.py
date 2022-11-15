set_n = set()
set_m = set()
first_numbers, second_numbers = [int(digit) for digit in input().split()]
for _ in range(first_numbers):
    current_number = int(input())
    set_n.add(current_number)
for _ in range(second_numbers):
    current_number = int(input())
    set_m.add(current_number)
for check_elements in set_n:
    if check_elements in set_m:
        print(check_elements)