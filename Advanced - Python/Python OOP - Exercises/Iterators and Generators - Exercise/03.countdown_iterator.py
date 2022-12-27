class countdown_iterator:

    def __init__(self, count):
        self.count = count
        self.end = count

    def __iter__(self):
        return self

    def __next__(self):
        if self.end == -1:
            raise StopIteration
        current_number = self.end
        self.end -= 1
        return current_number
