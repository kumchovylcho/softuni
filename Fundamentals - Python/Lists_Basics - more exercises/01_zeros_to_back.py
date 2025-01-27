def zeros_to_back(numbers: list[int]) -> list[int]:
    amount_of_zeros = numbers.count(0)
    # check if all the numbers are zero
    if len(numbers) == amount_of_zeros:
        return numbers

    # check if the zeros are already at the back
    if all(number == 0 for number in numbers[-amount_of_zeros:]):
        return numbers

    # move the zeros to the back
    shifted_times = 0
    while shifted_times < amount_of_zeros:
        numbers.append(numbers.pop(numbers.index(0)))
        shifted_times += 1

    return numbers


result = zeros_to_back([int(x) for x in input().split(", ")])
print(result)


########################################################################

# numbers_with_zeros = [int(number) for number in input().split(", ")]
#
# finding_the_zeros = [number for number in numbers_with_zeros if number == 0]
# numbers_without_zeros = [number for number in numbers_with_zeros if number > 0]
# list_with_zeros_at_the_back = numbers_without_zeros + finding_the_zeros
#
# print(list_with_zeros_at_the_back)
