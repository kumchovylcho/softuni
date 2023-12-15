from collections import deque

worms = [int(x) for x in input().split()]
holes = deque([int(x) for x in input().split()])

worms_length = len(worms)
matches = 0
while worms and holes:
    current_worm = worms.pop()
    current_hole = holes.popleft()

    if current_worm == current_hole:
        matches += 1
        continue

    current_worm -= 3
    if current_worm <= 0:
        continue

    worms.append(current_worm)


if matches:
    print(f"Matches: {matches}")
elif not matches:
    print("There are no matches.")


if not worms and matches == worms_length:
    print("Every worm found a suitable hole!")
elif not worms and matches != worms_length:
    print("Worms left: none")
elif worms:
    print(f"Worms left: {', '.join(str(x) for x in worms)}")


if not holes:
    print("Holes left: none")
elif holes:
    print(f"Holes left: {', '.join(str(x) for x in holes)}")