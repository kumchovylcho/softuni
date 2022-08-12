numbers = input().split()


def sort(lst):
    new_list = []
    for number in lst:
        number = int(number)
        new_list.append(number)
    return sorted(new_list)


print(sort(numbers))
