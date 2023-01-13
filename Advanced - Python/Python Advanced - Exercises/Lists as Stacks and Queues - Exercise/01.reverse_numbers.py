class Numbers:

    def __init__(self, numbers: list):
        self.numbers = numbers
        self.result = []

    def pop_last_number(self):
        return self.numbers.pop()

    def check_empty_list(self):
        return True if self.numbers else False

    def add_to_result(self, number):
        self.result.append(number)


items = input().split()
numbers = Numbers(items)
while numbers.numbers:
    if numbers.check_empty_list():
        popped_item = numbers.pop_last_number()
        numbers.add_to_result(popped_item)
print(' '.join(numbers.result))


# integers = input().split()
# reversed_integers = []
# for number in range(len(integers)):
#     reversed_integers.append(integers.pop())
# print(' '.join(reversed_integers))