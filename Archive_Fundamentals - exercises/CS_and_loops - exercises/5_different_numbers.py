lower_number, higher_number = int(input()), int(input())

if higher_number - lower_number < 5:
    print("No")
else:
    for first in range(lower_number, higher_number + 1):
        for second in range(lower_number, higher_number + 1):
            for third in range(lower_number, higher_number + 1):
                for forth in range(lower_number, higher_number + 1):
                    for fifth in range(lower_number, higher_number + 1):
                        if lower_number <= first < second < third < forth < fifth <= higher_number:
                            print(f"{first} {second} {third} {forth} {fifth}")