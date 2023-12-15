def create_matrix_and_find_player(field_size: int, player_symbol: str):
    player_row, player_col = 0, 0
    matrix = []
    for row in range(field_size):
        current_row = list(input())

        if player_symbol in current_row:
            player_row = row
            player_col = current_row.index(player_symbol)
            current_row[player_col] = "-"

        matrix.append(current_row)

    return matrix, player_row, player_col


def get_direction(direction: str):
    directions = {
        "up": (-1, 0),
        "down": (1, 0),
        "left": (0, -1),
        "right": (0, 1),
    }

    return directions[direction]


def valid_index(row: int, col: int, field_size: int):
    return 0 <= row < field_size and 0 <= col < field_size


def get_field_rewards(symbol: str):
    rewards = {
        "W": 100,
        "P": -200,
        "J": 100_000,
    }

    return rewards.get(symbol, 0)


def main():
    matrix_size = int(input())

    matrix, start_row, start_col = create_matrix_and_find_player(matrix_size, "G")
    money_left = 100

    command = input()
    while command != "end":
        next_row, next_col = get_direction(command)
        start_row += next_row
        start_col += next_col

        if not valid_index(start_row, start_col, matrix_size):
            print("Game over! You lost everything!")
            break

        money_left += get_field_rewards(matrix[start_row][start_col])
        matrix[start_row][start_col] = "-"
        if money_left > 20_001:
            print("You win the Jackpot!")
            print(f"End of the game. Total amount: {money_left}$")
            break

        if money_left <= 0:
            print("Game over! You lost everything!")
            break

        command = input()

    else:
        print(f"End of the game. Total amount: {money_left}$")

    if money_left > 0:
        matrix[start_row][start_col] = "G"
        for row in matrix:
            print("".join(row))


main()


