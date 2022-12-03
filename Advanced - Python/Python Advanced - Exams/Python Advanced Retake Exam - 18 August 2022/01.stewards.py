from collections import deque
free_seats = input().split(", ")
taken_seats = []
first_sequence = deque(input().split(", "))
second_sequence = deque(input().split(", "))
rotations = 0
while len(taken_seats) < 3 and rotations < 10:
    first_number = first_sequence[0]
    second_number = second_sequence[-1]
    character = chr(int(first_number) + int(second_number))
    if first_number + character in free_seats and first_number + character not in taken_seats:
        taken_seats.append(first_number + character)
        first_sequence.popleft()
        second_sequence.pop()
    elif second_number + character in free_seats and second_number + character not in taken_seats:
        taken_seats.append(second_number + character)
        first_sequence.popleft()
        second_sequence.pop()
    else:
        first_sequence.rotate(-1)
        second_sequence.rotate(1)
    rotations += 1
print(f"Seat matches: {', '.join(taken_seats)}")
print(f"Rotations count: {rotations}")
