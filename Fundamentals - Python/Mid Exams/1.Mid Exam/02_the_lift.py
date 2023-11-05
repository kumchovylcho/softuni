que_of_people = int(input())
lift_state = [int(x) for x in input().split()]

for i, wagon in enumerate(lift_state):
    people_to_add = 4 - wagon

    while people_to_add and que_of_people:
        people_to_add -= 1
        que_of_people -= 1
        lift_state[i] += 1


has_empty_wagons = len(lift_state) != lift_state.count(4)
if not que_of_people and has_empty_wagons:
    print("The lift has empty spots!")
elif que_of_people and not has_empty_wagons:
    print(f"There isn't enough space! {que_of_people} people in a queue!")

print(*lift_state, sep=" ")

##########################################################################################

# people_waiting = int(input())
# all_lifts = list(map(int, input().split()))
#
# for lift in range(len(all_lifts)):
#     people_added = min(4 - all_lifts[lift], people_waiting)
#     people_waiting -= people_added
#     all_lifts[lift] += people_added
#
# empty_spots = [x for x in all_lifts if x != 4]
# if not people_waiting and empty_spots:
#     print("The lift has empty spots!")
# elif people_waiting:
#     print(f"There isn't enough space! {people_waiting} people in a queue!")
# print(f"{' '.join(str(item) for item in all_lifts)}")

################################################################################################

# def add_people(all_lifts_list, index, people_remaining):
#     max_people_per_lift = 4
#     people_added = max_people_per_lift - all_lifts_list[index]
#     if people_remaining >= people_added:
#         all_lifts_list[index] += people_added
#         people_remaining -= people_added
#     elif people_remaining < people_added:
#         all_lifts_list[index] += people_remaining
#         people_remaining = 0
#     return all_lifts_list, people_remaining
#
#
# que_of_people = int(input())
# state_of_lifts = list(map(int, input().split()))
# for lift in range(len(state_of_lifts)):
#     if state_of_lifts[lift] < 4:
#         state_of_lifts, que_of_people = add_people(state_of_lifts, lift, que_of_people)
# check_for_empty_spots = [lift for lift in state_of_lifts if lift != 4]
# if check_for_empty_spots:
#     print("The lift has empty spots!")
# elif que_of_people:
#     print(f"There isn't enough space! {que_of_people} people in a queue!")
# print(' '.join(str(lift) for lift in state_of_lifts))


# que_for_the_lift = int(input())
# state_of_the_lift = [int(lift) for lift in input().split()]
#
#
# def space_on_lift(current_lift, taken_seats):
#     global que_for_the_lift
#     free_spots = 4 - taken_seats
#     if free_spots <= que_for_the_lift:
#         state_of_the_lift[current_lift] = taken_seats + free_spots
#         que_for_the_lift -= free_spots
#     elif free_spots > que_for_the_lift:
#         state_of_the_lift[current_lift] += que_for_the_lift
#         que_for_the_lift -= que_for_the_lift
#
#
# for lift_position, busy_seats in enumerate(state_of_the_lift):
#     if busy_seats < 4:
#         space_on_lift(lift_position, busy_seats)
#
#
# empty_spots = [spot for spot in state_of_the_lift if spot < 4]
# if not empty_spots and que_for_the_lift == 0:
#     print(*state_of_the_lift, end=" ")
#
# elif empty_spots:
#     print("The lift has empty spots!")
#     print(*state_of_the_lift, end=" ")
#
# elif not empty_spots:
#     print(f"There isn't enough space! {que_for_the_lift} people in a queue!")
#     print(*state_of_the_lift, end=" ")
