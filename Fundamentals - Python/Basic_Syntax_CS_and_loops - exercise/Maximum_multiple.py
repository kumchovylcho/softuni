divisor_number = int(input())
boundary_number = int(input())
for number in range(boundary_number, 0, -1):
    if number % divisor_number == 0:
        if number <= boundary_number and number > 0:
            print(number)
            break
