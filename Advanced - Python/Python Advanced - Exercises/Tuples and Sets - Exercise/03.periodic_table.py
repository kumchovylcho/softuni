class PeriodicTable:

    def __init__(self, number_of_lines: int):
        self.number_of_lines = number_of_lines
        self.unique_elements = set()

    def read_periodic_table(self):
        for _ in range(self.number_of_lines):
            [self.add_element(ele) for ele in input().split()]

    def add_element(self, item):
        self.unique_elements.add(item)


table = PeriodicTable(int(input()))
table.read_periodic_table()
print(*table.unique_elements, sep='\n')


# chemical_elements = int(input())
# unique_elements = set()
# for _ in range(chemical_elements):
#     current_element = input().split()
#     [unique_elements.add(element) for element in current_element]
# [print(element) for element in unique_elements]