from collections import deque
kids = deque(input().split())
skips = int(input())
while len(kids) > 1:
    kids.rotate(-skips)
    print(f"Removed {kids.pop()}")
print(f"Last is {''.join(kids)}")
