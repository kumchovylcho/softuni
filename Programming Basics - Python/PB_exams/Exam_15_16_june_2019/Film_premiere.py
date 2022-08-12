movie = input()
package_for_movie_food = input()
number_of_tickets = int(input())
price = 0
if movie == "John Wick":
    if package_for_movie_food == "Drink":
        price = 12
    elif package_for_movie_food == "Popcorn":
        price = 15
    else:
        price = 19
elif movie == "Star Wars":
    if package_for_movie_food == "Drink":
        price = 18
    elif package_for_movie_food == "Popcorn":
        price = 25
    else:
        price = 30
    if number_of_tickets >= 4:
        price *= 0.7
else:
    if package_for_movie_food == "Drink":
        price = 9
    elif package_for_movie_food == "Popcorn":
        price = 11
    else:
        price = 14
    if number_of_tickets == 2:
        price *= 0.85
total_price = price * number_of_tickets
print(f"Your bill is {total_price:.2f} leva.")
