from collections import deque

main_colors = ['red', 'yellow', 'blue']
secondary_colors = {
    'orange': ["yellow", "red"],
    'purple': ["red", "blue"],
    'green': ["yellow", "blue"]
}
colors_given = deque(input().split())
result = []
while colors_given:
    if len(colors_given) > 1:
        first_part = colors_given.popleft()
        second_part = colors_given.pop()
        color_name = first_part + second_part
        color_name_backwards = second_part + first_part
    elif len(colors_given) == 1:
        color_name = colors_given.pop()
        color_name_backwards = color_name
    if color_name not in main_colors and color_name_backwards not in main_colors and color_name not in secondary_colors\
            and color_name_backwards not in secondary_colors:
        if first_part and second_part:
            first_part, second_part = first_part[:-1], second_part[:-1]
        else:
            color_name = color_name[:-1]
        mid = len(colors_given) // 2
        if len(colors_given) % 2 == 0:
            if first_part:
                colors_given.insert(mid, first_part)
            if second_part:
                colors_given.insert(mid, second_part)
            elif color_name:
                colors_given.append(color_name)
        elif len(colors_given) % 2 != 0:
            if first_part:
                colors_given.insert(mid + 1, first_part)
            if second_part:
                colors_given.insert(mid + 1, second_part)
        continue
    if color_name in main_colors or color_name in secondary_colors:
        result.append(color_name)
        continue
    if color_name_backwards in main_colors or color_name_backwards in secondary_colors:
        result.append(color_name_backwards)
all_colors = ("red", "yellow", "blue", "orange", "purple", "green")
for color, requirement_colors in secondary_colors.items():
    for curr_color in requirement_colors:
        if curr_color not in result and color in result:
            result.remove(color)
            break
print(result)
