length_of_cake = int(input())
width_of_cake = int(input())
whole_cake = length_of_cake * width_of_cake
is_stopped = False
while whole_cake > 0:
    piece_of_cake = input()
    if piece_of_cake == "STOP":
        is_stopped = True
        break
    else:
        piece_of_cake = int(piece_of_cake)
        whole_cake -= piece_of_cake
        if whole_cake < 0:
            break

if is_stopped:
    print(f"{abs(whole_cake)} pieces are left.")
else:
    print(f"No more cake left! You need {abs(whole_cake)} pieces more.")
