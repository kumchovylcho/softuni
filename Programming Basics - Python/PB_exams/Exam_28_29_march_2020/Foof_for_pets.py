number_of_days = int(input())
total_food = float(input())
eaten_dog_food = 0
eaten_cat_food = 0
every_3_days = 0
for day in range(1, number_of_days + 1):
    eaten_food_by_dog = int(input())
    eaten_food_by_cat = int(input())
    eaten_dog_food += eaten_food_by_dog
    eaten_cat_food += eaten_food_by_cat
    if day % 3 == 0:
        every_3_days = every_3_days + (eaten_food_by_dog + eaten_food_by_cat) * 0.10
total_eaten_food = eaten_dog_food + eaten_cat_food
eaten_food = (total_eaten_food / total_food) * 100
dog = (eaten_dog_food / total_eaten_food) * 100
cat = (eaten_cat_food / total_eaten_food) * 100
print(f"Total eaten biscuits: {round(every_3_days)}gr.\n{eaten_food:.2f}% of the food has been eaten.")
print(f"{dog:.2f}% eaten from the dog.\n{cat:.2f}% eaten from the cat.")
