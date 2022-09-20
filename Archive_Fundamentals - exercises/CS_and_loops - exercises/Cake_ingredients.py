ingredient = input()
ingredient_counter = 0
while ingredient != "Bake!":
    print(f"Adding ingredient {ingredient}.")
    ingredient_counter += 1
    ingredient = input()
print(f"Preparing cake with {ingredient_counter} ingredients.")