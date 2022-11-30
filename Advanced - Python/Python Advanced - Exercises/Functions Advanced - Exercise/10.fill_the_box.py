def fill_the_box(*args):
    box_size = 1
    for size in args[:3]:
        box_size *= size
    for put_in_box in args[3:]:
        if put_in_box == "Finish":
            break
        box_size -= put_in_box
    if box_size >= 0:
        return f"There is free space in the box. You could put {box_size} more cubes."
    return f"No more free space! You have {abs(box_size)} more cubes."
