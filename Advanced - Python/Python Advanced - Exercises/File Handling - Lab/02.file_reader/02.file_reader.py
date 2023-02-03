def sum_of_numbers(file_name):
    with open(file_name, "r") as file:
        return sum(int(x) for x in file)


print(sum_of_numbers('numbers.txt'))
