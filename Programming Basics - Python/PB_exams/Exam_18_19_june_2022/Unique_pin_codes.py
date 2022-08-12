upper_limit_first_number = int(input())
upper_limit_second_number = int(input())
upper_limit_third_number = int(input())
prime_number = 2, 3, 5, 7
for first in range(1, upper_limit_first_number + 1):
    for second in range(1, upper_limit_second_number + 1):
        for third in range(1, upper_limit_third_number + 1):
            if first % 2 == 0 and third % 2 == 0 and second in prime_number:
                print(f"{first} {second} {third}")
