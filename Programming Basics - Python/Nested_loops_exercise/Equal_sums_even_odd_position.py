starting_number = int(input())
final_number = int(input())
for first_number in range(starting_number, final_number + 1):
    first_number_str = str(first_number)
    even_sum = 0
    odd_sum = 0
    for symbol in range(0, len(first_number_str)):
        number = int(first_number_str[symbol])
        if symbol % 2 == 0:
            even_sum += number
        else:
            odd_sum += number
    if even_sum == odd_sum:
        print(first_number_str, end=" ")
