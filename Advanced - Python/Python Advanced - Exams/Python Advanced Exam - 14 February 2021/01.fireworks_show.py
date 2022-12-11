from collections import deque


def create_firework(current_power):
    if current_power % 3 == 0 and current_power % 5 == 0:
        collected_fireworks['Crossette Fireworks'] += 1
        return True
    elif current_power % 5 == 0 and current_power % 3 != 0:
        collected_fireworks['Willow Fireworks'] += 1
        return True
    elif current_power % 3 == 0 and current_power % 5 != 0:
        collected_fireworks['Palm Fireworks'] += 1
        return True


fireworks = deque(int(x) for x in input().split(", ") if int(x) > 0)
explosive_power = deque(int(x) for x in input().split(", ") if int(x) > 0)
collected_fireworks = {
    'Palm Fireworks': 0,
    'Willow Fireworks': 0,
    'Crossette Fireworks': 0
}
is_perfect_show = False
while fireworks and explosive_power:
    current_firework = fireworks.popleft()
    current_explosive = explosive_power.pop()
    power_of_firework = current_firework + current_explosive
    is_created = create_firework(power_of_firework)
    if not is_created:
        if current_firework - 1 > 0:
            fireworks.append(current_firework - 1)
        explosive_power.append(current_explosive)
    ready_fireworks = [value for key, value in collected_fireworks.items() if value > 2]
    if len(ready_fireworks) == 3:
        is_perfect_show = True
        break
if is_perfect_show:
    print("Congrats! You made the perfect firework show!")
elif not is_perfect_show:
    print("Sorry. You can't make the perfect firework show.")
if fireworks:
    print(f"Firework Effects left: {', '.join(str(x) for x in fireworks)}")
if explosive_power:
    print(f"Explosive Power left: {', '.join(str(x) for x in explosive_power)}")
for firework, amount in collected_fireworks.items():
    print(f"{firework}: {amount}")