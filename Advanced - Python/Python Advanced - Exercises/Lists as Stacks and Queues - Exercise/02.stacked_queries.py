class Query:

    def __init__(self):
        self.stack = []

    def add_number(self, number: int):
        self.stack.append(number)

    def delete_number_at_top(self):
        self.stack.pop()

    def print_max_number(self):
        print(max(self.stack))

    def print_min_number(self):
        print(min(self.stack))

    def check_if_stack_empty(self):
        return False if self.stack else True


number_of_operations = int(input())
query = Query()
operations = {
    1: lambda x: query.add_number(x),
    2: query.delete_number_at_top,
    3: query.print_max_number,
    4: query.print_min_number
}
for _ in range(number_of_operations):
    command, *number = [int(x) for x in input().split()]
    if command != 1:
        if not query.check_if_stack_empty():
            operations[command]()
        continue
    operations[command](*number)
print(*query.stack[::-1], sep=", ")


# class Queries:
#
#     def __init__(self):
#         self.numbers = []
#
#     def push(self, current_number):
#         self.numbers.append(current_number)
#
#     def delete(self):
#         if self.numbers:
#             self.numbers.pop()
#
#     def print_maximum(self):
#         if self.numbers:
#             print(max(self.numbers))
#
#     def print_minimum(self):
#         if self.numbers:
#             print(min(self.numbers))
#
#
# stacked_queries = Queries()
# task_operations = {
#     1: stacked_queries.push,
#     2: stacked_queries.delete,
#     3: stacked_queries.print_maximum,
#     4: stacked_queries.print_minimum
# }
# number_of_lines = int(input())
# for line in range(number_of_lines):
#     command, *number = [int(number) for number in input().split()]
#     task_operations[command](*number)
# print(*stacked_queries.numbers[::-1], sep=', ')