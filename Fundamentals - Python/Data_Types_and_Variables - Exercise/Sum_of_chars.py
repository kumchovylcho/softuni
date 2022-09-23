number_of_letters = int(input())
list_with_letters = [ord(input()) for letter in range(number_of_letters)]
print(f"The sum equals: {sum(list_with_letters)}")


# number_of_letters = int(input())
# total = 0
# for letter in range(1, number_of_letters + 1):
#     current_letter = ord(input())
#     total += current_letter
# print(f"The sum equals: {total}")
