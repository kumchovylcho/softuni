number_of_painted_eggs = int(input())
red_colored_egg = 0
orange_colored_egg = 0
blue_colored_egg = 0
green_colored_egg = 0
max_eggs = 0
egg_color = None
for egg in range(1, number_of_painted_eggs + 1):
    color_of_the_egg = input()
    if color_of_the_egg == "red":
        red_colored_egg += 1
        if red_colored_egg > max_eggs:
            max_eggs = red_colored_egg
            egg_color = color_of_the_egg
    elif color_of_the_egg == "orange":
        orange_colored_egg += 1
        if orange_colored_egg > max_eggs:
            max_eggs = orange_colored_egg
            egg_color = color_of_the_egg
    elif color_of_the_egg == "blue":
        blue_colored_egg += 1
        if blue_colored_egg > max_eggs:
            max_eggs = blue_colored_egg
            egg_color = color_of_the_egg
    else:
        green_colored_egg += 1
        if green_colored_egg > max_eggs:
            max_eggs = green_colored_egg
            egg_color = color_of_the_egg
print(f"Red eggs: {red_colored_egg}\nOrange eggs: {orange_colored_egg}\nBlue eggs: {blue_colored_egg}")
print(f"Green eggs: {green_colored_egg}\nMax eggs: {max_eggs} -> {egg_color}")
