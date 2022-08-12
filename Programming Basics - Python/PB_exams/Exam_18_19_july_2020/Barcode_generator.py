first_barcode = input()
second_barcode = input()
first = first_barcode[0]
second = first_barcode[1]
third = first_barcode[2]
forth = first_barcode[3]
first_second = second_barcode[0]
second_second = second_barcode[1]
second_third = second_barcode[2]
second_forth = second_barcode[3]
for one in range(int(first), int(first_second) + 1):
    for two in range(int(second), int(second_second) + 1):
        for three in range(int(third), int(second_third) + 1):
            for four in range(int(forth), int(second_forth) + 1):
                if one % 2 != 0 and two % 2 != 0 and three % 2 != 0 and four % 2 != 0:
                    print(f"{one}{two}{three}{four}", end=" ")
