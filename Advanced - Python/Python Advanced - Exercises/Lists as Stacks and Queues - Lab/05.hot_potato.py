# from collections import deque
# kids = deque(input().split())
# skips = int(input())
# while len(kids) > 1:
#     kids.rotate(-skips)
#     print(f"Removed {kids.pop()}")
# print(f"Last is {''.join(kids)}")


kids = input().split()
skips = int(input())
index = 0
counter = 1
while len(kids) > 1:
    if 0 <= index < len(kids):
        if counter % skips == 0:
            print(f"Removed {kids.pop(index)}")
    else:
        index = 0
        counter += 1
        continue

    counter += 1
    index += 1
