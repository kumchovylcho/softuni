quantity_of_food = float(input()) * 1000
quantity_of_hay = float(input()) * 1000
quantity_of_cover = float(input()) * 1000
weight_of_guinea_pig = float(input()) * 1000
out_of_food = False
for day in range(1, 31):
    quantity_of_food -= 300
    if day % 2 == 0:
        quantity_of_hay -= quantity_of_food * 0.05
    if day % 3 == 0:
        quantity_of_cover -= weight_of_guinea_pig / 3
    if quantity_of_food <= 0 or \
            quantity_of_hay <= 0 or \
            quantity_of_cover <= 0:
        out_of_food = True

if out_of_food:
    print("Merry must go to the pet store!")
elif not out_of_food:
    quantity_of_food /= 1000
    quantity_of_hay /= 1000
    quantity_of_cover /= 1000
    print(f"Everything is fine! Puppy is happy! Food: {quantity_of_food:.2f}, Hay: {quantity_of_hay:.2f}, Cover: {quantity_of_cover:.2f}.")
