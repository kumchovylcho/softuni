factor_number = int(input())
counter_number = int(input())
multiples_of_factor_number = []
for number in range(1, counter_number + 1):
    result = factor_number * number
    multiples_of_factor_number.append(result)
print(multiples_of_factor_number)
