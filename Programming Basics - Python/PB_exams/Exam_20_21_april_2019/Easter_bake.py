from math import ceil
number_of_easter_breads = int(input())
flour = 750
sugar = 950
biggest_number_flour = 0
biggest_number_sugar = 0
total_sugar_used = 0
total_flour_used = 0
for bread in range(1, number_of_easter_breads + 1):
    quantity_used_sugar = int(input())
    quantity_used_flour = int(input())
    if quantity_used_sugar > biggest_number_sugar:
        biggest_number_sugar = quantity_used_sugar
    if quantity_used_flour > biggest_number_flour:
        biggest_number_flour = quantity_used_flour
    total_sugar_used += quantity_used_sugar
    total_flour_used += quantity_used_flour
flour_packages = ceil(total_flour_used / flour)
sugar_packages = ceil(total_sugar_used / sugar)
print(f"Sugar: {sugar_packages}\nFlour: {flour_packages}")
print(f"Max used flour is {biggest_number_flour} grams, max used sugar is {biggest_number_sugar} grams.")
