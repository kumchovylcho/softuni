number_of_lines = int(input())
even = []
odd = []
negative = []
positive = []
for lines in range(number_of_lines):
    current_number = int(input())
    if current_number % 2 == 0:
        even.append(current_number)
    if current_number % 2 != 0:
        odd.append(current_number)
    if current_number < 0:
        negative.append(current_number)
    if current_number >= 0:
        positive.append(current_number)
command = input()
if command == "even":
    print(even)
elif command == "odd":
    print(odd)
elif command == "negative":
    print(negative)
elif command == "positive":
    print(positive)
