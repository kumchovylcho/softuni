class Elements:

    def __init__(self):
        self.set_one = set()
        self.set_two = set()

    def add_element_first_set(self, current_element):
        self.set_one.add(current_element)

    def add_element_second_set(self, current_element):
        self.set_two.add(current_element)

    def find_intersection(self):
        return self.set_one.intersection(self.set_two)


elements = Elements()
n, m = [int(x) for x in input().split()]
for _ in range(n):
    curr_element = input()
    elements.add_element_first_set(curr_element)
for _ in range(m):
    curr_element = input()
    elements.add_element_second_set(curr_element)
result = elements.find_intersection()
print(*result, sep="\n")


# set_n = set()
# set_m = set()
# first_numbers, second_numbers = [int(digit) for digit in input().split()]
# for _ in range(first_numbers):
#     current_number = int(input())
#     set_n.add(current_number)
# for _ in range(second_numbers):
#     current_number = int(input())
#     set_m.add(current_number)
# for check_elements in set_n:
#     if check_elements in set_m:
#         print(check_elements)