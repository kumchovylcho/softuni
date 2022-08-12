from math import floor
from math import ceil
area_of_place = int(input())
grape_per_square_meter = float(input())
needed_liters_wine = int(input())
workers = int(input())
kgs_grape_for_production = (area_of_place * grape_per_square_meter) * 0.4
liters_wine = kgs_grape_for_production / 2.5
difference = abs(liters_wine - needed_liters_wine)
if liters_wine < needed_liters_wine:
    print(f"It will be a tough winter! More {floor(difference)} liters wine needed.")
else:
    print(f"Good harvest this year! Total wine: {floor(liters_wine)} liters.")
    for_workers = difference / workers
    print(f"{ceil(difference)} liters left -> {ceil(for_workers)} liters per person.")
