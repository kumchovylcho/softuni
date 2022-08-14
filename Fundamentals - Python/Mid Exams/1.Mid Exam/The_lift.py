que_for_the_lift = int(input())
state_of_the_lift = [int(lift) for lift in input().split()]


def space_on_lift(current_lift, taken_seats):
    global que_for_the_lift
    free_spots = 4 - taken_seats
    if free_spots <= que_for_the_lift:
        state_of_the_lift[current_lift] = taken_seats + free_spots
        que_for_the_lift -= free_spots
    elif free_spots > que_for_the_lift:
        state_of_the_lift[current_lift] += que_for_the_lift
        que_for_the_lift -= que_for_the_lift


for lift_position, busy_seats in enumerate(state_of_the_lift):
    if busy_seats < 4:
        space_on_lift(lift_position, busy_seats)


empty_spots = [spot for spot in state_of_the_lift if spot < 4]
if not empty_spots and que_for_the_lift == 0:
    print(*state_of_the_lift, end=" ")

elif empty_spots:
    print("The lift has empty spots!")
    print(*state_of_the_lift, end=" ")

elif not empty_spots:
    print(f"There isn't enough space! {que_for_the_lift} people in a queue!")
    print(*state_of_the_lift, end=" ")
