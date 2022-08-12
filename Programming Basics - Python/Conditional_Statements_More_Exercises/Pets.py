from math import ceil, floor
days = int(input())
left_food_kg = int(input())
daily_food_for_dog_kg = float(input())
daily_food_for_cat_kg = float(input())
daily_food_for_turtle_grams = float(input()) * 0.001
total_food_dog = daily_food_for_dog_kg * days
total_food_cat = daily_food_for_cat_kg * days
total_food_turtle = daily_food_for_turtle_grams * days
all_pets_food = total_food_dog + total_food_cat + total_food_turtle
if all_pets_food <= left_food_kg:
    leftover = left_food_kg - all_pets_food
    print(f"{floor(leftover)} kilos of food left.")
else:
    needed_food = all_pets_food - left_food_kg
    print(f"{ceil(needed_food)} more kilos of food are needed.")
