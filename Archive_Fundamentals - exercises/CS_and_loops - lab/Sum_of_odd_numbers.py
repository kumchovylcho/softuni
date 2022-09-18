odd_numbers = [number for number in range(1, int(input()) * 2, 2)]
[print(f"{number}") for number in odd_numbers]
print(f"Sum: {sum(odd_numbers)}")

# odd_numbers = int(input())
# total = 0
# for number in range(1, odd_numbers * 2, 2):
#     print(number)
#     total += number
# print(f"Sum: {total}")


# odd_numbers = int(input())
# counter = 0
# total = 0
# for number in range(1, 100, 2):
#     counter += 1
#     total += number
#     print(number)
#     if counter == odd_numbers:
#         break
# print(f"Sum: {total}")