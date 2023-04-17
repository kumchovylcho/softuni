control_number = int(input())
password_counter = 0
password = None
for a in range(1, 10):
    for b in range(1, 10):
        for c in range(1, 10):
            for d in range(1, 10):
                if (a * b) + (c * d) == control_number and a < b and c > d:
                    print(f"{a}{b}{c}{d}", end=" ")
                    password_counter += 1
                    if password_counter == 4:
                        password = f"{a}{b}{c}{d}"
if password_counter < 4:
    print("\nNo!")
elif password_counter >= 4:
    print(f"\nPassword: {password}")
