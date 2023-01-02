from collections import deque    # 83/100 , probably mistake with the steps


def find_kate_and_end_pos():
    kate_pos = ()
    end_points = []
    for row in range(len(matrix)):
        for col in range(len(matrix[0])):
            if matrix[row][col] == "k":
                kate_pos = row, col
            if row == 0 or row == rows - 1:
                if matrix[row][col] == " ":
                    end_points.append([row, col])
            if (col == 0 or col == len(matrix[0]) - 1) and row != 0 and row != rows - 1:
                if matrix[row][col] == " ":
                    end_points.append([row, col])
    return kate_pos, end_points


def find_neighbors(row, col):
    neighbors = []
    if row > 0:
        neighbors.append((row - 1, col))
    if row + 1 < len(matrix):
        neighbors.append((row + 1, col))
    if col > 0:
        neighbors.append((row, col - 1))
    if col + 1 < len(matrix[0]):
        neighbors.append((row, col + 1))

    return neighbors


def find_way_out(kate_pos):
    visited, queue, steps = set(), deque(), 1
    visited.add(kate_pos)
    queue.append([kate_pos[0], kate_pos[1]])
    while queue:
        current_pos = queue.popleft()
        check_neighbours = find_neighbors(current_pos[0], current_pos[1])
        for neighbours in check_neighbours:
            if neighbours in visited:
                continue
            row, col = neighbours
            if matrix[row][col] == "#" or matrix[row][col] == "k":
                continue
            visited.add(neighbours)
            queue.append([neighbours[0], neighbours[1]])
            steps += 1
            for index, exit_ in enumerate(all_exits):
                ex_r, ex_c = exit_
                if [row, col] == [ex_r, ex_c]:
                    all_exits.pop(index)
                    steps_to_get_out.append(steps)
                    matrix[row][col] = "#"
                    return


rows = int(input())
matrix = [[x for x in input()] for r in range(rows)]
steps_to_get_out = []
start_pos, all_exits = find_kate_and_end_pos()
find_way_out(start_pos)
if all_exits:
    find_way_out(start_pos)
if steps_to_get_out:
    print(f"Kate got out in {max(steps_to_get_out)} moves")
elif not steps_to_get_out:
    print("Kate cannot get out")
