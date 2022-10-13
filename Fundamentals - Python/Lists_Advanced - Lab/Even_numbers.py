numbers = [int(number) for number in input().split(", ")]
even_indexes = [index for index in range(len(numbers)) if numbers[index] % 2 == 0]
print(even_indexes)


# number_list = list(map(int, input().split(", ")))
# found_indices_or_no = map(
#     lambda x: x if number_list[x] % 2 == 0 else "no",
#     range(len(number_list)))
# even_indices = list(filter(lambda a: a != "no", found_indices_or_no))
# print(even_indices)