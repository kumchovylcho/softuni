first_number = int(input())
second_number = int(input())


def integer_to_base(number, to_base):
    result = ""
    while number != 0:
        result += str(number % to_base)
        number //= to_base
    return result[::-1]


print(integer_to_base(first_number, second_number))
