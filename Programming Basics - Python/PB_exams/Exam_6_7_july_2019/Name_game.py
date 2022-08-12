player_points = 0
total_player_points = 0
player_name = input()
first_player = ""
second_player = ""
while player_name != "Stop":
    for letter in player_name:
        number = int(input())
        if ord(letter) == number:
            total_player_points += 10
        else:
            total_player_points += 2
    if total_player_points >= player_points:
        player_points = total_player_points
        second_player = player_name
    total_player_points = 0
    player_name = input()
print(f"The winner is {second_player} with {player_points} points!")
