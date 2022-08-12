goal = int(input())
warming_up = goal - 30
fails = 0
jump_counter = 0
while fails < 3:
    current_jump = int(input())
    jump_counter += 1
    if current_jump > warming_up:
        warming_up += 5
        fails = 0
    else:
        fails += 1
    if warming_up > goal:
        print(f"Tihomir succeeded, he jumped over {goal}cm after {jump_counter} jumps.")
        exit()
print(f"Tihomir failed at {warming_up}cm after {jump_counter} jumps.")
