from sys import maxsize


class CustomList:

    def __init__(self):
        self.list = []

    def check_valid_index(self, index: int):
        if not 0 <= index < len(self.list):
            raise IndexError("Index out of range")

    def check_if_list_is_empty(self):
        return len(self.list) == 0

    def append(self, value):
        self.list.append(value)
        return self.list

    def remove(self, index: int):
        self.check_valid_index(index)

        if self.check_if_list_is_empty():
            return

        removed_item = self.list[index]
        del self.list[index]

        return removed_item

    def get(self, index: int):
        self.check_valid_index(index)

        if self.check_if_list_is_empty():
            return

        return self.list[index]

    def extend(self, iterable):
        self.append(iterable)

    def insert(self, index: int, value):
        self.check_valid_index(index)

        self.list.insert(index, value)

    def pop(self):
        if not self.list:
            raise ValueError("List is empty")

        removed_value = self.list[-1]
        del self.list[-1]

        return removed_value

    def clear(self):
        for i in range(len(self.list) - 1, -1, -1):
            self.remove(i)

    def index(self, value):
        for i in range(len(self.list)):
            if self.list[i] == value:
                return i

    def count(self, value):
        return sum(1 for item in self.list if item == value)

    def reverse(self):
        return self.list[::-1]

    def copy(self):
        return self.list[::]

    def size(self):
        return len(self.list)

    def add_first(self, value):
        self.insert(0, value)

    def dictionize(self):
        result = {}

        for i in range(0, len(self.list), 2):
            if i + 1 < len(self.list):
                result[self.list[i]] = self.list[i + 1]

            else:
                result[self.list[i]] = " "

        return result

    def move(self, amount: int):
        self.check_valid_index(amount)

        self.list = self.list[amount:] + self.list[:amount]

        return self.list

    def sum(self):
        result = 0

        for x in self.list:
            if isinstance(x, (int, float)):
                result += x

            else:
                result += len(x)

        return result

    def overbound(self):
        def check_for_bigger_value(current_value, current_max_value):
            if isinstance(item, (int, float)):
                if current_value > current_max_value:
                    return current_value

            else:
                if len(current_value) > current_max_value:
                    return len(current_value)

        biggest_value_index = 0
        biggest_value = -maxsize
        is_found = False

        for i in range(len(self.list)):
            item = self.list[i]

            result = check_for_bigger_value(item, biggest_value)
            if result:
                biggest_value_index = i
                biggest_value = result
                is_found = True

        if is_found:
            return biggest_value_index

    def underbound(self):
        def check_for_smaller_value(current_value, current_max_value):
            if isinstance(item, (int, float)):
                if current_value < current_max_value:
                    return current_value

            else:
                if len(current_value) < current_max_value:
                    return len(current_value)

        smallest_value_index = 0
        smallest_value = maxsize
        is_found = False

        for i in range(len(self.list)):
            item = self.list[i]

            result = check_for_smaller_value(item, smallest_value)
            if result:
                smallest_value_index = i
                smallest_value = result
                is_found = True

        if is_found:
            return smallest_value_index
