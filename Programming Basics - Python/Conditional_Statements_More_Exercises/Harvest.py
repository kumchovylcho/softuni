from math import ceil, floor
m2_wine = int(input())
grape_per_m2 = float(input())
needed_liters_wine = int(input())
number_of_workers = int(input())
kgs_of_grape = m2_wine * grape_per_m2
total_wine = (kgs_of_grape * 0.40) / 2.5
wine_left = total_wine - needed_liters_wine
wine_for_workers = wine_left / number_of_workers
if total_wine >= needed_liters_wine:
    print(f"Good harvest this year! Total wine: {floor(total_wine)} liters.\n{ceil(wine_left)} liters left -> {ceil(wine_for_workers)} liters per person.")
else:
    diff = needed_liters_wine - total_wine
    print(f"It will be a tough winter! More {floor(diff)} liters wine needed.")
