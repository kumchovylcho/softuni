def reverse_text(string):
    start_letter = len(string) - 1
    while start_letter >= 0:
        yield string[start_letter]
        start_letter -= 1
