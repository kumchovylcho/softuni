goal = 10000
current_steps = 0
is_reached = False
while current_steps < goal:
    steps = input()
    if steps == "Going home":
        steps_to_home = int(input())
        current_steps += steps_to_home
        if current_steps < 10000:
            is_reached = True
            break
    else:
        current_steps += int(steps)
diff = abs(goal - current_steps)
if is_reached:
    print(f"{diff} more steps to reach goal.")
else:
    print(f"Goal reached! Good job!\n{diff} steps over the goal!")
