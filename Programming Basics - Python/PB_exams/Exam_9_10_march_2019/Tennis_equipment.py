from math import floor, ceil
price_of_tennis_racket = float(input())
number_of_tennis_rackets = int(input())
number_of_boots = int(input())
price_tennis_rackets = price_of_tennis_racket * number_of_tennis_rackets
price_boots = (price_of_tennis_racket / 6) * number_of_boots
other_equipment = (price_tennis_rackets + price_boots) * 0.2
total_price = price_tennis_rackets + price_boots + other_equipment
djokovic_payment = floor(total_price / 8)
sponsors = ceil(total_price * 7 / 8)
print(f"Price to be paid by Djokovic {djokovic_payment}")
print(f"Price to be paid by sponsors {sponsors}")
