from math import sqrt


start_first_half = int(input())
start_second_half = int(input())


diff_first_half = int(input())
diff_second_half = int(input())


for one in range(start_first_half, start_first_half + diff_first_half + 1):
    for two in range(start_second_half, start_second_half + diff_second_half + 1):
        are_both_prime = True

        for number in one, two:
            if number < 2 or len(str(number)) < 2:
                continue

            for i in range(2, int(sqrt(number)) + 1):
                if number % i == 0:
                    are_both_prime = False
                    break

        if not are_both_prime:
            continue

        print(f"{one}{two}")