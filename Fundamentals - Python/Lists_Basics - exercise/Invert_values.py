numbers = input()
lst = numbers.split(" ")
new_list = list()
for number in lst:
    current_number = int(number)
    if current_number < 0:
        current_number = abs(current_number)
    else:
        current_number = -abs(current_number)
    new_list.append(current_number)
print(new_list)
