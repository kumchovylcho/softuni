total = 0
is_negative = False
contribution = input()
while contribution != "NoMoreMoney":
    contribution = float(contribution)
    if contribution > 0:
        print(f"Increase: {contribution:.2f}")
        total += contribution
    elif contribution < 0:
        is_negative = True
        break
    contribution = input()
if contribution == "NoMoreMoney":
    print(f"Total: {total:.2f}")
if is_negative:
    print("Invalid operation!")
    print(f"Total: {total:.2f}")