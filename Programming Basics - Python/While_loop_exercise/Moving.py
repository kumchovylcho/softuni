length_of_free_space = int(input())
width_of_free_space = int(input())
height_of_free_space = int(input())
free_space = length_of_free_space * width_of_free_space * height_of_free_space
is_done = False
while free_space > 0:
    number_of_boxes = input()
    if number_of_boxes == "Done":
        is_done = True
        break
    else:
        number_of_boxes = int(number_of_boxes)
        free_space -= number_of_boxes
if is_done:
    print(f"{free_space} Cubic meters left.")
else:
    print(f"No more free space! You need {abs(free_space)} Cubic meters more.")
