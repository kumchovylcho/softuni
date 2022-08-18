row_1 = [int(number) for number in input().split()]
row_2 = [int(number) for number in input().split()]
row_3 = [int(number) for number in input().split()]
first_player_wins = False
second_player_wins = False
draw = False


def game():
    global first_player_wins, second_player_wins, draw
    if (row_1[0] == 1 and row_2[0] == 1 and row_3[0] == 1) or \
        (row_1[1] == 1 and row_2[1] == 1 and row_3[1] == 1) or \
        (row_1[2] == 1 and row_2[2] == 1 and row_3[2] == 1) or \
        (row_1[0] == 1 and row_2[1] == 1 and row_3[2] == 1) or \
        (row_1[2] == 1 and row_2[1] == 1 and row_3[0] == 1) or \
        (row_1[0] == 1 and row_1[1] == 1 and row_1[2] == 1) or \
        (row_2[0] == 1 and row_2[1] == 1 and row_2[2] == 1) or \
        (row_3[0] == 1 and row_3[1] == 1 and row_3[2] == 1):
        first_player_wins = True

    elif (row_1[0] == 2 and row_2[0] == 2 and row_3[0] == 2) or \
        (row_1[1] == 2 and row_2[1] == 2 and row_3[1] == 2) or \
        (row_1[2] == 2 and row_2[2] == 2 and row_3[2] == 2) or \
        (row_1[0] == 2 and row_2[1] == 2 and row_3[2] == 2) or \
        (row_1[2] == 2 and row_2[1] == 2 and row_3[0] == 2) or \
        (row_1[0] == 2 and row_1[1] == 2 and row_1[2] == 2) or \
        (row_2[0] == 2 and row_2[1] == 2 and row_2[2] == 2) or \
        (row_3[0] == 2 and row_3[1] == 2 and row_3[2] == 2):
        second_player_wins = True

    else:
        draw = True

    return first_player_wins, second_player_wins, draw


game()

if first_player_wins:
    print("First player won")
elif second_player_wins:
    print("Second player won")
elif draw:
    print("Draw!")