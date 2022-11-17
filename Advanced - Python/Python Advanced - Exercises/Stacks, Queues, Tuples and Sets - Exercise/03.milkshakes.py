from collections import deque
chocolates = deque(int(choco) if choco[-1].isdigit() else choco for choco in input().split(", "))
cups_of_milk = deque(int(milk) if milk[-1].isdigit() else milk for milk in input().split(", "))
milkshakes_goal = 5
made_milkshakes = 0
while chocolates and cups_of_milk and made_milkshakes < milkshakes_goal:
    removed_below_zero = False
    if chocolates[-1] <= 0:
        chocolates.pop()
        removed_below_zero = True
    if cups_of_milk[0] <= 0:
        cups_of_milk.popleft()
        removed_below_zero = True
    if not removed_below_zero:
        if chocolates[-1] == cups_of_milk[0]:
            made_milkshakes += 1
            chocolates.pop()
            cups_of_milk.popleft()
        elif chocolates[-1] != cups_of_milk[0]:
            cups_of_milk.append(cups_of_milk.popleft())
            chocolates[-1] -= 5
if made_milkshakes == milkshakes_goal:
    print("Great! You made all the chocolate milkshakes needed!")
elif made_milkshakes < milkshakes_goal:
    print("Not enough milkshakes.")
if chocolates:
    print(f"Chocolate: {', '.join(str(x) for x in chocolates)}")
elif not chocolates:
    print("Chocolate: empty")
if cups_of_milk:
    print(f"Milk: {', '.join(str(x) for x in cups_of_milk)}")
elif not cups_of_milk:
    print("Milk: empty")