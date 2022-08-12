price_of_vacation = float(input())
puzzles = int(input())
talking_dolls = int(input())
teddy_bears = int(input())
minions = int(input())
trucks = int(input())
puzzle = 2.60 * puzzles
doll = 3 * talking_dolls
bear = 4.10 * teddy_bears
minion = 8.20 * minions
truck = 2 * trucks
total_count_of_toys = puzzles + talking_dolls + teddy_bears + minions + trucks
total_price = puzzle + doll + bear + minion + truck
if total_count_of_toys >= 50:
    total_price *= 0.75
total_price *= 0.90  # for rent
if total_price >= price_of_vacation:
    diff = total_price - price_of_vacation
    print(f"Yes! {diff:.2f} lv left.")
else:
    diff = price_of_vacation - total_price
    print(f"Not enough money! {diff:.2f} lv needed.")
