iterations = int(input())
for digits in range(1, iterations + 1):
    if digits >= 10:
        digits = str(digits)
        sum = int(digits[0]) + int(digits[1])
        if sum == 5 or sum == 7 or sum == 11:
            print(f"{digits} -> True")
        else:
            print(f"{digits} -> False")
    elif digits < 10:
        if digits == 5 or digits == 7:
            print(f"{digits} -> True")
        else:
            print(f"{digits} -> False")