def solution():
    def integers():
        i = 1
        while True:
            yield i
            i += 1

    def halves():
        for number in integers():
            yield number / 2

    def take(number, sequence):
        rotations = 0
        result = []
        for digit in halves():
            if rotations == number:
                return result
            result.append(digit)
            rotations += 1

    return take, halves, integers


take = solution()[0]
halves = solution()[1]
print(take(5, halves()))