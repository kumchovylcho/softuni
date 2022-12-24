class vowels:

    def __init__(self, string):
        self.string = string
        self.vowels = [v for v in self.string if v.lower() in "aeiuyo"]
        self.start = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.start == len(self.vowels):
            raise StopIteration
        index = self.start
        self.start += 1
        return self.vowels[index]
