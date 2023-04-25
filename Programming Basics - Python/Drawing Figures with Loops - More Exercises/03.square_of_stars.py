rows_and_columns = int(input())

for _ in range(rows_and_columns):
    print(" ".join("*" * rows_and_columns))





# for i in range(1, rows_and_columns + 1):
#     for j in range(1, rows_and_columns * 2 + 1):
#         if j % 2 != 0:
#             print("*", end="")
#
#         elif j % 2 == 0:
#             print(" ", end="")
#     print()