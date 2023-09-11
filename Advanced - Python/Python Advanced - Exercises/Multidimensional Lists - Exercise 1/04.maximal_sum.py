rows, width = map(int, input().split())

matrix = []
for _ in range(rows):
    matrix.append([int(n) for n in input().split()])


quadrants = {}
for row in range(rows - 2):
    for col in range(width - 2):

        nums = []
        for s_row in range(row, row + 3):
            nums.append(matrix[s_row][col : col + 3])

        total_sum = sum(sum(row) for row in nums)
        quadrants[total_sum] = nums

highest_sum = max(quadrants)
print(f'Sum = {highest_sum}')
for single_row in quadrants[highest_sum]:
    print(*single_row, sep=' ')



# from sys import maxsize
# rows, cols = [int(x) for x in input().split()]
# matrix = [[int(x) for x in input().split()] for _ in range(rows)]
# max_sum = -maxsize
# best_combo = []
# for row in range(rows):
#     for col in range(cols):
#         if 0 <= row + 3 <= rows and 0 <= col + 3 <= cols:
#             current_combo = []
#             current_sum = 0
#             for row_ in range(row, row + 3):
#                 result = matrix[row_][col:col + 3]
#                 current_combo.append(result)
#                 current_sum += sum(result)
#             if current_sum > max_sum:
#                 max_sum = current_sum
#                 best_combo = current_combo
# print(f"Sum = {max_sum}")
# for _row in range(len(best_combo)):
#     print(*best_combo[_row], sep=' ')
