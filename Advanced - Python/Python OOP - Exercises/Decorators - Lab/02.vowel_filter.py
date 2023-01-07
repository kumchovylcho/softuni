import functools


def vowel_filter(func):
    vowels = "aeioyu"

    @functools.wraps(func)
    def wrapper():
        return [letter for letter in func() if letter.lower() in vowels]
    return wrapper


@vowel_filter
def get_letters():
    return ["a", "b", "c", "d", "e"]


print(get_letters())