from math import ceil
average_speed = float(input())
litres_needed_for_100_km = float(input())
hours_to_go_to_the_moon = ceil((384400 * 2) / average_speed) + 3
fuel_needed = ((384400 * 2) * litres_needed_for_100_km) // 100
print(hours_to_go_to_the_moon)
print(int(fuel_needed))
