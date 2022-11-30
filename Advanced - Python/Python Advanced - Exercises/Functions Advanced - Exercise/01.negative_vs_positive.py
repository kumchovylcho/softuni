def find_positives(all_numbers):
    return sum([digit for digit in all_numbers if digit > 0])


def find_negatives(all_numbers):
    return sum([digit for digit in all_numbers if digit < 0])


def check_biggest_number(positive, negative):
    if abs(positive) > abs(negative):
        return "The positives are stronger than the negatives"
    return "The negatives are stronger than the positives"


numbers = [int(x) for x in input().split() if x[-1].isdigit()]
positives = find_positives(numbers)
negatives = find_negatives(numbers)
print(f"{negatives}\n{positives}")
print(check_biggest_number(positives, negatives))