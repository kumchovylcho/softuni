def find_tunnels():
    tunnel_positions = []
    for row in range(matrix_size):
        for col in range(len(matrix[row])):
            if matrix[row][col] == "T":
                tunnel_positions.append([row, col])
    return tunnel_positions


def check_index(row, col):
    if 0 <= row < matrix_size and 0 <= col < matrix_size:
        return True


def move(direction, is_finished, current_kms, car_row, car_col, tunnels_pos):
    for where, row, col in ('up', -1, 0), ('down', 1, 0), ('right', 0, 1), ('left', 0, -1):
        row, col = row + car_row, col + car_col
        if where == direction and check_index(row, col):
            if matrix[row][col] != "T" and matrix[row][col] != "F":
                current_kms += 10
            elif matrix[row][col] == "T":
                teleport_location = [x for x in tunnels_pos if x != [row, col]]
                matrix[row][col] = "."
                teleport_row, teleport_col = teleport_location[0][0], teleport_location[0][1]
                matrix[teleport_row][teleport_col] = "."
                current_kms += 30
                row, col = teleport_row, teleport_col
            elif matrix[row][col] == "F":
                is_finished = True
                current_kms += 10
            return is_finished, current_kms, [row, col]
    return is_finished, current_kms, [car_row, car_col]


def show_result(is_finished, row, col):
    matrix[row][col] = "C"
    if is_finished:
        print(f"Racing car {name_of_car} finished the stage!")
    elif not is_finished:
        print(f"Racing car {name_of_car} DNF.")
    print(f"Distance covered {kilometers} km.")
    [print(''.join(matrix[row])) for row in range(matrix_size)]


matrix_size = int(input())
name_of_car = input()
matrix = [[x for x in input().split()] for _ in range(matrix_size)]
finished, kilometers = False, 0
tunnels = find_tunnels()
car_position = [0, 0]
command = input()
while command != "End" and not finished:
    finished, kilometers, car_position = move(command, finished, kilometers, *car_position, tunnels)
    command = input()
show_result(finished, *car_position)
