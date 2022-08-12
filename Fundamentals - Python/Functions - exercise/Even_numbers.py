numbers = input().split()


def get_even_numbers(number):
    lst_with_even_numbers = []
    for num in number:
        num = int(num)
        if num % 2 == 0:
            lst_with_even_numbers.append(num)
    return lst_with_even_numbers


print(get_even_numbers(numbers))