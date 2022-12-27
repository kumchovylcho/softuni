class take_skip:

    def __init__(self, step, count):
        self.start = 0
        self.step = step
        self.count = count
        self.number = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.start == self.count:
            raise StopIteration
        self.start += 1
        current_number = self.number
        self.number += self.step
        return current_number
