count_of_numbers = int(input())
all_numbers = [input() for number in range(count_of_numbers)]
print(*all_numbers[::-1])
