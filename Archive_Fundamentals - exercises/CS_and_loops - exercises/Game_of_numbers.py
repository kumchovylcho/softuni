lower_number, higher_number, magical_number = int(input()), int(input()), int(input())
combinations = 0

for lower in range(higher_number, lower_number - 1, -1):
    for higher in range(higher_number, lower_number - 1, -1):
        if higher + lower == magical_number:
            break
        else:
            combinations += 1
    if higher + lower == magical_number:
        break
if higher + lower == magical_number:
    print(f"Number found! {lower} + {higher} = {lower + higher}")
else:
    print(f"{combinations} combinations - neither equals {magical_number}")