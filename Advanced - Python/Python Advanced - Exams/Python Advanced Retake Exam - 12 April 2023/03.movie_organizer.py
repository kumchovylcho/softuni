def movie_organizer(*args):
    movies = {}

    for m_name, genre in args:
        movies[genre] = movies.get(genre, []) + [m_name]


    sorted_movies = dict(sorted(movies.items(), key=lambda x: (-len(x[1]), x[0])))

    output = []
    for genre, movies in sorted_movies.items():
        output.append(f"{genre} - {len(movies)}")

        for movie_name in sorted(movies):
            output.append(f"* {movie_name}")


    return '\n'.join(output)


print(movie_organizer(
    ("The Matrix", "Sci-fi")))


print(movie_organizer(
    ("The Godfather", "Drama"),
    ("The Hangover", "Comedy"),
    ("The Shawshank Redemption", "Drama"),
    ("The Pursuit of Happiness", "Drama"),
    ("The Hangover Part II", "Comedy")))


print(movie_organizer(
    ("Avatar: The Way of Water", "Action"),
    ("House Of Gucci", "Drama"),
    ("Top Gun", "Action"),
    ("Ted", "Comedy"),
    ("Duck Soup", "Comedy"),
    ("The Dark Knight", "Action"),
    ("A Star Is Born", "Musicals"),
    ("The Warrior", "Action"),
    ("Like A Boss", "Comedy"),
    ("The Green Mile", "Drama"),
    ("21 Jump Street", "Comedy")))