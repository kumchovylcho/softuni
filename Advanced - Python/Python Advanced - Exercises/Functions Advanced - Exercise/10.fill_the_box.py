def fill_the_box(*args):
    current_box = args[0] * args[1] * args[2]
    fill_box = 0

    for box in args[3:]:
        if box == "Finish":
            break
        fill_box += box

    if current_box >= fill_box:
        free_space = current_box - fill_box
        return f"There is free space in the box. You could put {free_space} more cubes."
    return f"No more free space! You have {fill_box - current_box} more cubes."


# def fill_the_box(*args):
#     box_size = 1
#     for size in args[:3]:
#         box_size *= size
#     for put_in_box in args[3:]:
#         if put_in_box == "Finish":
#             break
#         box_size -= put_in_box
#     if box_size >= 0:
#         return f"There is free space in the box. You could put {box_size} more cubes."
#     return f"No more free space! You have {abs(box_size)} more cubes."


print(fill_the_box(2, 8, 2, 2, 1, 7, 3, 1, 5, "Finish"))
print(fill_the_box(5, 5, 2, 40, 11, 7, 3, 1, 5, "Finish"))
print(fill_the_box(10, 10, 10, 40, "Finish", 2, 15, 30))
