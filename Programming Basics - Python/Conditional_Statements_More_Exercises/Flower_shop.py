from math import floor, ceil
number_of_magnolias = int(input())
number_of_hyacinths = int(input())
number_of_roses = int(input())
number_of_cactuses = int(input())
price_of_the_gift = float(input())
magnolia = 3.25 * number_of_magnolias
hyacinths = 4 * number_of_hyacinths
rose = 3.50 * number_of_roses
cactus = 8 * number_of_cactuses
taxes = 0.95
total_price = magnolia + hyacinths + rose + cactus
total_price *= taxes
if total_price >= price_of_the_gift:
    diff = total_price - price_of_the_gift
    print(f"She is left with {floor(diff)} leva.")
else:
    diff = price_of_the_gift - total_price
    print(f"She will have to borrow {abs(ceil(diff))} leva.")
