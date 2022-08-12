number_of_eggs_first_player = int(input())
number_of_eggs_second_player = int(input())
winner = input()
while winner != "End":
    if winner == "one":
        number_of_eggs_second_player -= 1
        if number_of_eggs_second_player == 0:
            print(f"Player two is out of eggs. Player one has {number_of_eggs_first_player} eggs left.")
            break
    elif winner == "two":
        number_of_eggs_first_player -= 1
        if number_of_eggs_first_player == 0:
            print(f"Player one is out of eggs. Player two has {number_of_eggs_second_player} eggs left.")
            break
    winner = input()
if winner == "End":
    print(f"Player one has {number_of_eggs_first_player} eggs left.\nPlayer two has {number_of_eggs_second_player} eggs left.")
