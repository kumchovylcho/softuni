class Queries:

    def __init__(self):
        self.numbers = []

    def push(self, current_number):
        self.numbers.append(current_number)

    def delete(self):
        if self.numbers:
            self.numbers.pop()

    def print_maximum(self):
        if self.numbers:
            print(max(self.numbers))

    def print_minimum(self):
        if self.numbers:
            print(min(self.numbers))


stacked_queries = Queries()
task_operations = {
    1: stacked_queries.push,
    2: stacked_queries.delete,
    3: stacked_queries.print_maximum,
    4: stacked_queries.print_minimum
}
number_of_lines = int(input())
for line in range(number_of_lines):
    command, *number = [int(number) for number in input().split()]
    task_operations[command](*number)
print(*stacked_queries.numbers[::-1], sep=', ')