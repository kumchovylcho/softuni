starting_number = int(input())
final_number = int(input())
magic_number = int(input())
is_magic = False
counter_of_combinations = 0
for first_number in range(starting_number, final_number + 1):
    for second_number in range(starting_number, final_number + 1):
        counter_of_combinations += 1
        if first_number + second_number == magic_number:
            is_magic = True
            break
    if is_magic:
        break
if is_magic:
    print(f"Combination N:{counter_of_combinations} ({first_number} + {second_number} = {magic_number})")
else:
    print(f"{counter_of_combinations} combinations - neither equals {magic_number}")
