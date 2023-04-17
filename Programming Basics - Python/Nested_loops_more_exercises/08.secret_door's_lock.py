from math import sqrt

hundreds_border = int(input())
dozens_border = int(input())
units_border = int(input())


for h in range(1, hundreds_border + 1):
    if h % 2 != 0:
        continue

    for d in range(1, dozens_border + 1):
        if d < 2:
            continue

        is_prime = True
        for i in range(2, int(sqrt(d)) + 1):
            if d % i == 0:
                is_prime = False
                break

        if not is_prime:
            continue

        for u in range(1, units_border + 1):
            if u % 2 != 0:
                continue

            print(f"{h} {d} {u}")