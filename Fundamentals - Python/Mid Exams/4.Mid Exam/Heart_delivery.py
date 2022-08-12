neighborhood = [int(num) for num in input().split("@")]
last_house = 0


def jump_on_houses(current_jump, last_house_jumped):
    last_house_jumped += current_jump
    if last_house_jumped >= len(neighborhood):
        last_house_jumped = 0
    if 0 <= last_house_jumped < len(neighborhood):
        if neighborhood[last_house_jumped] >= 2:
            neighborhood[last_house_jumped] -= 2
            if neighborhood[last_house_jumped] == 0:
                print(f"Place {last_house_jumped} has Valentine's day.")
        elif neighborhood[last_house_jumped] == 0:
            print(f"Place {last_house_jumped} already had Valentine's day.")
    return last_house_jumped


jump = input()
while jump != "Love!":
    jump = jump.split()
    jump = int(jump[1])
    last_house = jump_on_houses(jump, last_house)
    jump = input()

print(f"Cupid's last position was {last_house}.")

cupid_fails = 0
for hearts in neighborhood:
    if hearts != 0:
        cupid_fails += 1

if cupid_fails == 0:
    print("Mission was successful.")
elif cupid_fails > 0:
    print(f"Cupid has failed {cupid_fails} places.")
