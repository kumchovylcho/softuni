class dictionary_iter:

    def __init__(self, dictionary: dict):
        self.dictionary = list(dictionary.items())
        self.start = 0
        self.end = len(self.dictionary)

    def __iter__(self):
        return self

    def __next__(self):
        if self.start == self.end:
            raise StopIteration
        result = self.dictionary[self.start]
        self.start += 1
        return result
