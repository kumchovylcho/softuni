from math import floor
number_of_balls = int(input())
red_color = 5
orange_color = 10
yellow_color = 15
white_color = 20
total_points = 0
# black color divides the total points by 2 and floors it
red_balls = 0
orange_balls = 0
yellow_balls = 0
white_balls = 0
black_balls = 0
other_colors = 0
for num in range(1, number_of_balls + 1):
    current_ball_color = input()
    if current_ball_color == "red":
        total_points += red_color
        red_balls += 1
    elif current_ball_color == "orange":
        total_points += orange_color
        orange_balls += 1
    elif current_ball_color == "yellow":
        total_points += yellow_color
        yellow_balls += 1
    elif current_ball_color == "white":
        total_points += white_color
        white_balls += 1
    elif current_ball_color == "black":
        total_points = floor(total_points / 2)
        black_balls += 1
    else:
        other_colors += 1
print(f"Total points: {total_points}\nRed balls: {red_balls}\nOrange balls: {orange_balls}")
print(f"Yellow balls: {yellow_balls}\nWhite balls: {white_balls}\nOther colors picked: {other_colors}")
print(f"Divides from black balls: {black_balls}")
