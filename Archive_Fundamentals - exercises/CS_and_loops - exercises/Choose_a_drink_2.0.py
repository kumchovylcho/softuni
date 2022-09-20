profession, quantity = input(), int(input())


drink_chooser = {
    'Athlete': 0.70,
    'Businessman': 1,
    'Businesswoman': 1,
    'SoftUni Student': 1.70
}

if profession in drink_chooser:
    print(f"The {profession} has to pay {drink_chooser[profession] * quantity:.2f}.")
else:
    print(f"The {profession} has to pay {1.20 * quantity:.2f}.")
