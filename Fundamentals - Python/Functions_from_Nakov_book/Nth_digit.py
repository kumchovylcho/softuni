number = input()
number_to_print = int(input())


def get_number(string, show_number):
    result = string[-show_number]
    return result


print(get_number(number, number_to_print))