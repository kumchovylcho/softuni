number_of_lines = int(input())
all_numbers = [int(input()) for _ in range(number_of_lines)]
positives = [number for number in all_numbers if number >= 0]
negatives = [number for number in all_numbers if number < 0]
print(f"{positives}\n{negatives}")
print(f"Count of positives: {len(positives)}")
print(f"Sum of negatives: {sum(negatives)}")


# number_of_lines = int(input())
# positives = []
# negatives = []
# for lines in range(number_of_lines):
#     number = int(input())
#     if number >= 0:
#         positives.append(number)
#     else:
#         negatives.append(number)
# print(positives)
# print(negatives)
# print(f"Count of positives: {len(positives)}")
# print(f"Sum of negatives: {sum(negatives)}")
