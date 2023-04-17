starter_number = int(input())
ending_number = int(input())
for first_number in range(starter_number, ending_number + 1):
    for second_number in range(starter_number, ending_number + 1):
        for third_number in range(starter_number, ending_number + 1):
            for forth_number in range(starter_number, ending_number + 1):
                if ((first_number % 2 == 0 and forth_number % 2 != 0) or (first_number % 2 != 0 and forth_number % 2 == 0)) and \
                        first_number > forth_number and ((second_number + third_number) % 2) == 0:
                    print(f"{first_number}{second_number}{third_number}{forth_number}", end=" ")

