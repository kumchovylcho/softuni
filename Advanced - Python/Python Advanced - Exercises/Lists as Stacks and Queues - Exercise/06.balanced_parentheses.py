from collections import deque

parentheses = deque(input())
open_per = deque()
balanced = True
while parentheses:
    check_par = parentheses.popleft()
    if check_par in "{[(":
        open_per.append(check_par)
    elif not open_per:
        balanced = False
        break
    else:
        check_last_par = open_per.pop()
        test_pair = f"{check_last_par + check_par}"
        if test_pair not in "{}()[]":
            balanced = False
            break

if balanced and not open_per:
    print("YES")
else:
    print("NO")

