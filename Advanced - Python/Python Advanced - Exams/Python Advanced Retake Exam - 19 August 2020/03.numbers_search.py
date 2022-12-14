def numbers_searching(*args):
    duplicates = []
    for number in sorted(args):
        if args.count(number) > 1 and number not in duplicates:
            duplicates.append(number)
    unique_numbers = set(range(min(args), max(args)))
    missing_number = unique_numbers.difference(args)
    duplicates = [*missing_number, duplicates]
    return duplicates


# def numbers_searching(*args):
#     number_not_in, duplicate_numbers = 0, []
#     min_number, max_number = min(args), max(args)
#     for n in range(min_number, max_number + 1):
#         if n not in args:
#             number_not_in = n
#         if args.count(n) > 1 and n not in duplicate_numbers:
#             duplicate_numbers.append(n)
#     duplicate_numbers.sort()
#     return [number_not_in, duplicate_numbers]
