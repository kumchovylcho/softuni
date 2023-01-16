class Battle:

    def __init__(self):
        self.even_set = set()
        self.odd_set = set()

    def sum_ascii_values(self, current_name: str):
        return sum(ord(x) for x in current_name)

    def check_even_or_odd_result(self, sum_of_ascii: int):
        return sum_of_ascii % 2 == 0

    def divide_to_current_row(self, current_row: int, sum_of_ascii: int):
        return sum_of_ascii // current_row

    def check_if_sum_is_equal(self):
        return sum(self.even_set) == sum(self.odd_set)

    def check_if_sum_odd_is_bigger(self):
        return sum(self.odd_set) > sum(self.even_set)

    def show_result(self):
        if self.check_if_sum_is_equal():
            return self.odd_set.union(self.even_set)
        if self.check_if_sum_odd_is_bigger():
            return self.odd_set.difference(self.even_set)
        return self.odd_set.symmetric_difference(self.even_set)


battle_of_names = Battle()
number_of_names = int(input())
for row in range(1, number_of_names + 1):
    name = input()
    sum_ascii = battle_of_names.sum_ascii_values(name)
    sum_ascii = battle_of_names.divide_to_current_row(row, sum_ascii)
    if battle_of_names.check_even_or_odd_result(sum_ascii):
        battle_of_names.even_set.add(sum_ascii)
        continue
    battle_of_names.odd_set.add(sum_ascii)
print(*battle_of_names.show_result(), sep=", ")


# number_of_names = int(input())
# even_sum = set()
# odd_sum = set()
# for row in range(1, number_of_names + 1):
#     name = input()
#     result = sum(ord(letter) for letter in name) // row
#     if result % 2 == 0:
#         even_sum.add(result)
#     elif result % 2 != 0:
#         odd_sum.add(result)
# if sum(even_sum) == sum(odd_sum):
#     print(*odd_sum.union(even_sum), sep=', ')
# elif sum(odd_sum) > sum(even_sum):
#     print(*odd_sum.difference(even_sum), sep=', ')
# elif sum(even_sum) > sum(odd_sum):
#     print(*odd_sum.symmetric_difference(even_sum), sep=', ')