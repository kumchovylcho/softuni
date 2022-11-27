def locate_bunny(row, col):
    for row in range(len(matrix)):
        for col in range(len(matrix[row])):
            if matrix[row][col] == "B":
                return [row, col]


def check_best_corridor(bunny_row, bunny_col):
    for direction, row, col in (("up", -1, 0), ("down", 1, 0), ("left", 0, -1), ("right", 0, 1)):
        bunny_move_row, bunny_move_col, num, coor = bunny_row + row, bunny_col + col, 0, []
        for jump in range(cols):
            if 0 <= bunny_move_row < rows and 0 <= bunny_move_col < cols and matrix[bunny_move_row][bunny_move_col] != "X":
                num += matrix[bunny_move_row][bunny_move_col]
                coor.append([bunny_move_row, bunny_move_col])
                bunny_move_row, bunny_move_col = row + bunny_move_row, col + bunny_move_col
            else:
                result[num] = {direction: coor}
                break


def show_result():
    if sum(result) != 0:
        best_corridor = max(result)
        for direction, road in result[best_corridor].items():
            print(direction)
            for indexes in road:
                print(indexes)
            print(best_corridor)


result = {}
rows = int(input())
cols = rows
matrix = [[int(x) if x[-1].isdigit() else x for x in input().split()] for _ in range(rows)]
bunny_index = locate_bunny(rows, cols)
check_best_corridor(*bunny_index)
show_result()
