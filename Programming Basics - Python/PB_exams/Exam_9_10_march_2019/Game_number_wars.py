first_player_name = input()
second_player_name = input()
score_first_player = 0
score_second_player = 0
first_player_card = input()
while first_player_card != "End of game":
    second_player_card = input()
    int_first_player = int(first_player_card)
    int_second_player = int(second_player_card)
    if int_first_player > int_second_player:
        score_first_player += int_first_player - int_second_player
    elif int_second_player > int_first_player:
        score_second_player += int_second_player - int_first_player
    elif int_first_player == int_second_player:
        first_player_card = int(input())
        second_player_card = int(input())
        if first_player_card > second_player_card:
            print(f"Number wars!\n{first_player_name} is winner with {score_first_player} points")
            break
        elif second_player_card > first_player_card:
            print(f"Number wars!\n{second_player_name} is winner with {score_second_player} points")
            break
    first_player_card = input()
if first_player_card == "End of game":
    print(f"{first_player_name} has {score_first_player} points")
    print(f"{second_player_name} has {score_second_player} points")
