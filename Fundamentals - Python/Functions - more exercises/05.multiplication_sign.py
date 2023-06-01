def check_numbers(first, second, third):
    if any(x == 0 for x in (first, second, third)):
        return "zero"

    if all(x > 0 for x in (first, second, third)) or \
            sum(1 for x in (first, second, third) if x < 0) == 2:
        return "positive"

    return "negative"


first_number = int(input())
second_number = int(input())
third_number = int(input())

print(check_numbers(first_number,
                    second_number,
                    third_number
                    )
      )


# def check_numbers(first, second, third):
#     if (first > 0 and second > 0 and third > 0) or \
#             (first > 0 and second < 0 and third < 0) or \
#             (second > 0 and first < 0 and third < 0) or \
#             (third > 0 and first < 0 and second < 0):
#         print("positive")
#     elif first == 0 or second == 0 or third == 0:
#         print("zero")
#     elif first < 0 or second < 0 or third < 0:
#         print("negative")
#
#
# first_number = int(input())
# second_number = int(input())
# third_number = int(input())
#
#
# check_numbers(first_number, second_number, third_number)
