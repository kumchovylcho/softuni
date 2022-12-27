class sequence_repeat:

    def __init__(self, text, repeat_times):
        self.text = text
        self.repeat_times = repeat_times
        self.counter = 0
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.counter == self.repeat_times:
            raise StopIteration
        index = self.index
        if self.index >= len(self.text):
            self.index = 0
            index = 0
        self.index += 1
        self.counter += 1
        return self.text[index]
