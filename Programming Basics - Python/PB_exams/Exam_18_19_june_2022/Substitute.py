K = int(input())
L = int(input())
M = int(input())
N = int(input())
changes_counter = 0
for first_number in range(K, 8 + 1):
    for second_number in range(9, L - 1, -1):
        for third_number in range(M, 8 + 1):
            for forth_number in range(9, N - 1, -1):
                if first_number % 2 == 0 and third_number % 2 == 0 and second_number % 2 != 0 and forth_number % 2 != 0:
                    if first_number == third_number and second_number == forth_number:
                        print("Cannot change the same player.")
                    else:
                        print(f"{first_number}{second_number} - {third_number}{forth_number}")
                        changes_counter += 1
                        if changes_counter == 6:
                            exit()
