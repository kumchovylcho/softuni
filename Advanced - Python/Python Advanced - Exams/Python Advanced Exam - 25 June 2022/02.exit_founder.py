def move(current_player, row, col):
    if matrix[row][col] == "E":
        players[current_player]['won'] = True
        print(f"{current_player} found the Exit and wins the game!")
    elif matrix[row][col] == "T":
        players[current_player]['trapped'] = True
        winner = ''.join([name for name in players if current_player != name])
        print(f"{current_player} is out of the game! The winner is {winner}.")
    elif matrix[row][col] == "W":
        players[current_player]['rest'] = True
        print(f"{current_player} hits a wall and needs to rest.")


matrix_size = 6
tom_and_jerry = input().split(", ")
matrix = [[col for col in input().split()] for row in range(matrix_size)]
player_one, player_two = tom_and_jerry[0], tom_and_jerry[1]
players = {
    player_one: {'trapped': False, 'won': False, 'rest': False},
    player_two: {'trapped': False, 'won': False, 'rest': False}
}
counter = 1
while not players[player_one]['trapped'] and not players[player_one]['won'] and not \
     players[player_two]['trapped'] and not players[player_two]['won']:
    next_position = input()
    row, col = int(next_position[1]), int(next_position[-2])
    if counter % 2 != 0:
        if not players[player_one]['rest']:
            move(player_one, row, col)
        elif players[player_one]['rest']:
            players[player_one]['rest'] = False
    else:
        if not players[player_two]['rest']:
            move(player_two, row, col)
        elif players[player_two]['rest']:
            players[player_two]['rest'] = False
    counter += 1

