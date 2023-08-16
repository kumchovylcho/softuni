k = int(input())
l = int(input())
m = int(input())
n = int(input())

changes_made = 0

for first_first in range(k, 8 + 1):
    if first_first % 2 == 1:
        continue

    for second_first in range(9, l - 1, -1):
        if second_first % 2 == 0:
            continue

        for first_second in range(m, 8 + 1):
            if first_second % 2 == 1:
                continue

            for second_second in range(9, n - 1, -1):
                if second_second % 2 == 0:
                    continue

                if str(first_first) + str(second_first) == str(first_second) + str(second_second):
                    print("Cannot change the same player.")
                    continue

                changes_made += 1
                print(f"{first_first}{second_first} - {first_second}{second_second}")

                if changes_made == 6:
                    break
            if changes_made == 6:
                break
        if changes_made == 6:
            break
    if changes_made == 6:
        break




# K = int(input())
# L = int(input())
# M = int(input())
# N = int(input())
# changes_counter = 0
# for first_number in range(K, 8 + 1):
#     for second_number in range(9, L - 1, -1):
#         for third_number in range(M, 8 + 1):
#             for forth_number in range(9, N - 1, -1):
#                 if first_number % 2 == 0 and third_number % 2 == 0 and second_number % 2 != 0 and forth_number % 2 != 0:
#                     if first_number == third_number and second_number == forth_number:
#                         print("Cannot change the same player.")
#                     else:
#                         print(f"{first_number}{second_number} - {third_number}{forth_number}")
#                         changes_counter += 1
#                         if changes_counter == 6:
#                             exit()
