number = int(input())

for numbers in range(1, number + 1):
    if numbers < 10:
        if numbers == 5 or numbers == 7:
            print(f"{numbers} -> True")
        else:
            print(f"{numbers} -> False")
    if numbers >= 10:
        numbers = str(numbers)
        first_digit = int(numbers[0])
        second_digit = int(numbers[1])
        total = first_digit + second_digit
        if total == 5 or total == 7 or total == 11:
            print(f"{numbers} -> True")
        else:
            print(f"{numbers} -> False")
