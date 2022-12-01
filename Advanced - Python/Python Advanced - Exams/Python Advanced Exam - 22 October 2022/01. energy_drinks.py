from collections import deque
caffeine = deque(int(x) for x in input().split(", ") if x.isdigit())
energy_drinks = deque(int(x) for x in input().split(", ") if x.isdigit())
max_allowed_caffeine = 300
accepted_caffeine = 0
while caffeine and energy_drinks:
    current_caffeine = caffeine.pop()
    energy = energy_drinks[0]
    result = current_caffeine * energy
    if result + accepted_caffeine <= max_allowed_caffeine:
        energy_drinks.popleft()
        accepted_caffeine += result
    elif result + accepted_caffeine > max_allowed_caffeine:
        energy_drinks.rotate(-1)
        accepted_caffeine -= 30
        if accepted_caffeine < 0:
            accepted_caffeine = 0
if energy_drinks:
    print(f"Drinks left: {', '.join(str(x) for x in energy_drinks)}")
elif not energy_drinks:
    print("At least Stamat wasn't exceeding the maximum caffeine.")
print(f"Stamat is going to sleep with {accepted_caffeine} mg caffeine.")
