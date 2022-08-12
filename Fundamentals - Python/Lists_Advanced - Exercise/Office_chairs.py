number_of_rooms = int(input())
free_chairs = 0
enough_chairs = False


def free_chair(chair, visitor):
    result = abs(chair - visitor)
    print(f"{result} more chairs needed in room {room}")


def not_enough_chairs(chair, visitor):
    result = chair - visitor
    return result


for room in range(1, number_of_rooms + 1):
    current_room = input().split()
    chairs = len(current_room[0])
    visitors = int(current_room[1])
    if chairs - visitors < 0:
        free_chair(chairs, visitors)
        enough_chairs = True
    elif chairs - visitors > 0:
        free_chairs += not_enough_chairs(chairs, visitors)

if not enough_chairs:
    print(f"Game On, {free_chairs} free chairs left")
