number = int(input())
for first_number in range(number):
    for second_number in range(number):
        for third_number in range(number):
            print(f"{chr(97 + first_number)}{chr(97 + second_number)}{chr(97 + third_number)}")
