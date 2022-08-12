number = int(input())
for first_number in range(1, 10):
    for second_number in range(1, 10):
        for third_number in range(1, 10):
            for forth_number in range(1, 10):
                if first_number + second_number == third_number + forth_number:
                    if number % (first_number + second_number) == 0:
                        print(f"{first_number}{second_number}{third_number}{forth_number}", end=" ")