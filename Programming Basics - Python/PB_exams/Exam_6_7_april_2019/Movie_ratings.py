import sys
movies_that_Desi_likes = int(input())
movie_lowest_rating = sys.maxsize
movie_highest_rating = -sys.maxsize
highest_movie_rating = ""
lowest_movie_rating = ""
total_rating = 0
for movie in range(1, movies_that_Desi_likes + 1):
    name_of_movie = input()
    rating_of_the_movie = float(input())
    total_rating += rating_of_the_movie
    if rating_of_the_movie > movie_highest_rating:
        movie_highest_rating = rating_of_the_movie
        highest_movie_rating = name_of_movie
    elif rating_of_the_movie < movie_lowest_rating:
        movie_lowest_rating = rating_of_the_movie
        lowest_movie_rating = name_of_movie
average_rating = total_rating / movies_that_Desi_likes
print(f"{highest_movie_rating} is with highest rating: {movie_highest_rating:.1f}")
print(f"{lowest_movie_rating} is with lowest rating: {movie_lowest_rating:.1f}")
print(f"Average rating: {average_rating:.1f}")
