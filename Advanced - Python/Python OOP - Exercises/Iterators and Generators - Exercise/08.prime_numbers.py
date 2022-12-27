def get_primes(integers):
    for digit in integers:
        if digit > 1:
            for num in range(2, digit):
                if digit % num == 0:
                    break
            else:
                yield digit
