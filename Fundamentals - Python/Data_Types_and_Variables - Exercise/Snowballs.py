highest_snowball_value = 0
biggest_weight = 0
biggest_time = 0
biggest_quality = 0
number_of_snowballs = int(input())
for snowball in range(1, number_of_snowballs + 1):
    weight = int(input())
    time_in_air = int(input())
    quality_of_snowball = int(input())
    current_snowball = (weight / time_in_air) ** quality_of_snowball
    if current_snowball > highest_snowball_value:
        highest_snowball_value = current_snowball
        biggest_weight = weight
        biggest_time = time_in_air
        biggest_quality = quality_of_snowball
print(f"{biggest_weight} : {biggest_time} = {int(highest_snowball_value)} ({biggest_quality})")
