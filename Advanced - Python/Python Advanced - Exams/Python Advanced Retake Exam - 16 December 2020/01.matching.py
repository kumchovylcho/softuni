from collections import deque

males = deque(int(x) for x in input().split())
females = deque(int(x) for x in input().split())
matches = 0
while males and females:
    if females[0] <= 0:
        females.popleft()
        continue
    if males[-1] <= 0:
        males.pop()
        continue
    if males[-1] % 25 == 0:
        males.pop()
        males.pop()
        continue
    if females[0] % 25 == 0:
        females.popleft()
        females.popleft()
        continue
    current_male = males.pop()
    current_female = females.popleft()
    if current_male == current_female:
        matches += 1
        continue
    males.append(current_male - 2)
print(f"Matches: {matches}")
if not males:
    print("Males left: none")
elif males:
    print(f"Males left: {', '.join(str(x) for x in reversed(males))}")
if not females:
    print("Females left: none")
elif females:
    print(f"Females left: {', '.join(str(x) for x in females)}")
