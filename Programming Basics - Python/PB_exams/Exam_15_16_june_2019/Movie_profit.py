name_of_movie = input()
number_of_days = int(input())
number_of_tickets = int(input())
price_per_ticket = float(input())
percent_for_the_cinema = int(input())
total_money = (number_of_tickets * price_per_ticket) * number_of_days
total_money_left = total_money - (total_money * (percent_for_the_cinema / 100))
print(f"The profit from the movie {name_of_movie} is {total_money_left:.2f} lv.")
