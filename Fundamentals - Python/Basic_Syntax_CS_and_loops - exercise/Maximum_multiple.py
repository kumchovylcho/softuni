divisor_number, boundary_number = int(input()), int(input())
for number in range(boundary_number, 0, -1):
    if number % divisor_number == 0 and number <= boundary_number > 0:
        print(number)
        break
