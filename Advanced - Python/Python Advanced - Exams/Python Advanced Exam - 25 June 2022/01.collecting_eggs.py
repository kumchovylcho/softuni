from collections import deque
eggs_size = deque(int(x) for x in input().split(", "))
paper_size = deque(int(x) for x in input().split(", "))
box_size = 50
filled_boxes = 0
while eggs_size and paper_size:
    current_egg = eggs_size.popleft()
    current_paper_size = paper_size.pop()
    if abs(current_egg) == 13:
        paper_size.rotate(-1)
        paper_size.appendleft(current_paper_size)
    elif current_egg <= 0:
        paper_size.append(current_paper_size)
    elif current_egg > 0 and current_egg + current_paper_size <= box_size:
        filled_boxes += 1
if filled_boxes:
    print(f"Great! You filled {filled_boxes} boxes.")
elif not filled_boxes:
    print(f"Sorry! You couldn't fill any boxes!")
if eggs_size:
    print(f"Eggs left: {', '.join(str(x) for x in eggs_size)}")
if paper_size:
    print(f"Pieces of paper left: {', '.join(str(x) for x in paper_size)}")