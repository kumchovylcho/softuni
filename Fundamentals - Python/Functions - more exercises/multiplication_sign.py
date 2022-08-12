first_number = int(input())
second_number = int(input())
third_number = int(input())


def check_numbers(first, second, third):
    if (first > 0 and second > 0 and third > 0) or \
            (first > 0 and second < 0 and third < 0) or \
            (second > 0 and first < 0 and third < 0) or \
            (third > 0 and first < 0 and second < 0):
        print("positive")
    elif first == 0 or second == 0 or third == 0:
        print("zero")
    elif first < 0 or second < 0 or third < 0:
        print("negative")


check_numbers(first_number, second_number, third_number)
