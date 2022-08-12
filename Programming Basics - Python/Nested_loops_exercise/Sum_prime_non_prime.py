sum_of_prime_numbers = 0
sum_of_non_prime_numbers = 0
number = input()
while number != "stop":
    number = int(number)
    if number < 0:
        print("Number is negative.")
        number = input()
        continue
    counter = 0
    for digit in range(1, number + 1):
        if number % digit == 0:
            counter += 1
    if counter == 2:
        sum_of_prime_numbers += number
    else:
        sum_of_non_prime_numbers += number
    number = input()
print(f"Sum of all prime numbers is: {sum_of_prime_numbers}")
print(f"Sum of all non prime numbers is: {sum_of_non_prime_numbers}")
