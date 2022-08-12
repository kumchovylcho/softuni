from math import floor
name_of_series = input()
number_of_seasons = int(input())
number_of_episodes = int(input())
length_of_episode = float(input())
episode_with_advertises = length_of_episode * 0.2 + length_of_episode
extra_long_episode_for_end_season = number_of_seasons * 10
total_minutes = (number_of_seasons * episode_with_advertises) * number_of_episodes + extra_long_episode_for_end_season
print(f"Total time needed to watch the {name_of_series} series is {floor(total_minutes)} minutes.")
