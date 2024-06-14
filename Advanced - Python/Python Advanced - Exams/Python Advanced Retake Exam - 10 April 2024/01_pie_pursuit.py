from collections import deque


contestants = deque(int(x) for x in input().split())
pies = [int(x) for x in input().split()]

while contestants and pies:
    contestant = contestants.popleft()
    pie = pies.pop()

    if contestant >= pie:
        contestant -= pie
        if contestant > 0:
            contestants.append(contestant)

    elif pie > contestant:
        pie -= contestant
        if pie == 1 and pies:
            pies[-1] += pie
        elif pie != 1 or pie > 0:
            pies.append(pie)


if not pies and contestants:
    print("We will have to wait for more pies to be baked!")
    print(f"Contestants left: {', '.join(str(x) for x in contestants)}")
elif not contestants and not pies:
    print("We have a champion!")
elif not contestants and pies:
    print("Our contestants need to rest!")
    print(f"Pies left: {', '.join(str(x) for x in pies)}")
