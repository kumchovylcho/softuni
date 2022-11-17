from collections import deque
bees = deque(int(bee) for bee in input().split())
nectar = deque(int(nectar) for nectar in input().split())
symbols = deque(input().split())
collected_honey = 0
while bees and nectar:
    if bees[0] <= nectar[-1]:
        symbol = symbols.popleft()
        if symbol == '+':
            collected_honey += bees[0] + nectar[-1]
        elif symbol == '-':
            collected_honey += abs(bees[0] - nectar[-1])
        elif symbol == '*':
            collected_honey += abs(bees[0] * nectar[-1])
        elif symbol == '/':
            if bees[0] > 0 and nectar[-1] > 0:
                collected_honey += abs(bees[0] / nectar[-1])
        bees.popleft()
    nectar.pop()
print(f"Total honey made: {collected_honey}")
if bees:
    print(f"Bees left: {', '.join(str(x) for x in bees)}")
if nectar:
    print(f"Nectar left: {', '.join(str(x) for x in nectar)}")