time_for_photos = int(input())
number_of_scenes = int(input())
time_length_of_a_scene = int(input())
preparing_terrain = int(time_for_photos * 0.15)
minutes_scene = number_of_scenes * time_length_of_a_scene
total_minutes = minutes_scene + preparing_terrain
diff = abs(total_minutes - time_for_photos)
if total_minutes < time_for_photos:
    print(f"You managed to finish the movie on time! You have {round(diff)} minutes left!")
else:
    print(f"Time is up! To complete the movie you need {diff} minutes.")
