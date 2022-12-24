def squares(end_number):
    num = 1
    while num <= end_number:
        yield num * num
        num += 1

