from collections import deque
cups = deque([int(cup) for cup in input().split()])
bottles = [int(bottle) for bottle in input().split()]
wasted_water = 0
while cups and bottles:
    if bottles[-1] >= cups[0]:
        wasted_water += bottles[-1] - cups[0]
        cups.popleft()
        bottles.pop()
    elif bottles[-1] < cups[0]:
        cups[0] -= bottles[-1]
        bottles.pop()
        if cups[0] <= 0:
            cups.popleft()
if not cups:
    print(f"Bottles: {' '.join(str(bottle) for bottle in bottles)}")
elif not bottles:
    print(f"Cups: {' '.join(str(cup) for cup in cups)}")
print(f"Wasted litters of water: {wasted_water}")