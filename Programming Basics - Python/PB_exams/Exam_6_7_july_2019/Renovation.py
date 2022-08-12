from math import ceil
height_of_the_wall = int(input())
width_of_the_wall = int(input())
space_that_wont_be_painted = int(input()) / 100
free_space = height_of_the_wall * width_of_the_wall * 4
space_for_painting = ceil(free_space - (free_space * space_that_wont_be_painted))
painted_space = 0
is_more = False
is_perfect = False
litres_paint = input()
while litres_paint != "Tired!":
    litres_paint = int(litres_paint)
    painted_space += litres_paint
    if painted_space > space_for_painting:
        is_more = True
        break
    if painted_space == space_for_painting:
        is_perfect = True
        break
    litres_paint = input()
diff = abs(space_for_painting - painted_space)
if is_more:
    print(f"All walls are painted and you have {diff} l paint left!")
elif is_perfect:
    print(f"All walls are painted! Great job, Pesho!")
else:
    print(f"{diff} quadratic m left.")
