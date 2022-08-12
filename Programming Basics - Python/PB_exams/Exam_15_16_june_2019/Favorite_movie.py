import string
movie_counter = 0
movie_with_most_points = 0
current_movie_score = 0
favorite_movie = None
lower_letters = string.ascii_lowercase
upper_letters = string.ascii_uppercase
movie_title = input()
while movie_title != "STOP":
    movie_counter += 1
    for letter in movie_title:
        if letter in lower_letters:
            current_movie_score += ord(letter) - (len(movie_title) * 2)
        elif letter in upper_letters:
            current_movie_score += ord(letter) - (len(movie_title))
        else:
            current_movie_score += ord(letter)
    if current_movie_score > movie_with_most_points:
        favorite_movie = movie_title
        movie_with_most_points = current_movie_score
    if movie_counter == 7:
        print(f"The limit is reached.")
        print(f"The best movie for you is {favorite_movie} with {movie_with_most_points} ASCII sum.")
        break
    current_movie_score = 0
    movie_title = input()
if movie_title == "STOP":
    print(f"The best movie for you is {favorite_movie} with {movie_with_most_points} ASCII sum.")
