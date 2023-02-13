def check_valid_index(check_row, check_col):
    if 0 <= check_row < rows and 0 <= check_col < len(matrix[check_row]):
        return True


def attack_ship(attack_row, attack_col, field: list):
    if field[attack_row][attack_col] > 0:
        field[attack_row][attack_col] -= 1
        if field[attack_row][attack_col] == 0:
            return field, 1
    return field, 0


rows = int(input())
matrix = [[int(x) for x in input().split()] for _ in range(rows)]
targets_position = input().split()

destroyed_ships = 0

for pos in targets_position:
    row, col = [int(x) for x in pos.split("-")]

    if check_valid_index(row, col):
        matrix, down_ship = attack_ship(row, col, matrix)
        destroyed_ships += down_ship

print(destroyed_ships)
