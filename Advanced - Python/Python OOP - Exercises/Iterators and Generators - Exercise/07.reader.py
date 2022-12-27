def read_next(*args):
    for element in args:
        for symbol in element:
            yield symbol
