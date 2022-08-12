number = int(input())
counter = 1
for numbers in range(1, number + 1):
    if counter < 10:
        if counter == 5 or counter == 7:
            print(f"{counter} -> True")
        else:
            print(f"{counter} -> False")
    if counter >= 10:
        numbers = str(numbers)
        first_digit = int(numbers[0])
        second_digit = int(numbers[1])
        total = first_digit + second_digit
        if total == 5 or total == 7 or total == 11:
            print(f"{counter} -> True")
        else:
            print(f"{counter} -> False")
    counter += 1
