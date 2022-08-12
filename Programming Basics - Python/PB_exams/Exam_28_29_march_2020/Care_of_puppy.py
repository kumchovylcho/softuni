dog_food_kg = int(input()) * 1000
eaten_food = 0
eaten_food_daily = input()
while eaten_food_daily != "Adopted":
    eaten_food += int(eaten_food_daily)
    eaten_food_daily = input()
if eaten_food_daily == "Adopted":
    if dog_food_kg >= eaten_food:
        left_over = dog_food_kg - eaten_food
        print(f"Food is enough! Leftovers: {left_over} grams.")
    elif dog_food_kg < eaten_food:
        food_needed = eaten_food - dog_food_kg
        print(f"Food is not enough. You need {abs(food_needed)} grams more.")
