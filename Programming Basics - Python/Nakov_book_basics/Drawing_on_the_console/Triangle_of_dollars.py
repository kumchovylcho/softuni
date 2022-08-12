dollars = int(input())
for dollar in range(1, dollars + 1):
    if dollar > 1:
        print("$ " * dollar)
    else:
        print("$" * dollar)
