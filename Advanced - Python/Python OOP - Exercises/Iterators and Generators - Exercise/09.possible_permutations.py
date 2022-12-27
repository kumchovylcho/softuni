from itertools import permutations


def possible_permutations(items):
    for item in permutations(items):
        yield list(item)
