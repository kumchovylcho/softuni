number_of_lines = int(input())
all_numbers = [int(input()) for _ in range(number_of_lines)]
command = input()
if command == "even":
    all_numbers = [number for number in all_numbers if number % 2 == 0]
elif command == "odd":
    all_numbers = [number for number in all_numbers if number % 2 != 0]
elif command == "negative":
    all_numbers = [number for number in all_numbers if number < 0]
elif command == "positive":
    all_numbers = [number for number in all_numbers if number >= 0]

print(all_numbers)


# number_of_lines = int(input())
# even = []
# odd = []
# negative = []
# positive = []
# for lines in range(number_of_lines):
#     current_number = int(input())
#     if current_number % 2 == 0:
#         even.append(current_number)
#     if current_number % 2 != 0:
#         odd.append(current_number)
#     if current_number < 0:
#         negative.append(current_number)
#     if current_number >= 0:
#         positive.append(current_number)
# command = input()
# if command == "even":
#     print(even)
# elif command == "odd":
#     print(odd)
# elif command == "negative":
#     print(negative)
# elif command == "positive":
#     print(positive)
