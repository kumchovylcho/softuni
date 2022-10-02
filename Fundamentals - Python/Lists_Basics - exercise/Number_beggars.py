money_for_beggars = [int(number) for number in input().split(", ")]
number_of_beggars = int(input())
index_of_beggar = 0
earned_money = []
while index_of_beggar < number_of_beggars:
    total = 0
    for beggar in range(index_of_beggar, len(money_for_beggars), number_of_beggars):
        total += money_for_beggars[beggar]
    earned_money.append(total)
    index_of_beggar += 1
print(earned_money)


# first_line = input()
# second_line = int(input())
#
# first_line = first_line.split(",")
# total_list = shuffled_cards()
# old_list = shuffled_cards()
# length_of_first = len(first_line)
#
# if length_of_first < second_line:
#     for number in first_line:
#         total_list.append(int(number))
#     for number in range(abs(length_of_first - second_line)):
#         total_list.append(0)
#
#
# elif length_of_first == second_line:
#     for number in first_line:
#         total_list.append(int(number))
#
# else:
#     for number in first_line:
#         old_list.append(int(number))
#     for _ in range(0, second_line):
#         total_list.append(sum(old_list[_::second_line]))
#
# print(total_list)
