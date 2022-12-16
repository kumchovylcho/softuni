from collections import deque


def check_if_the_bombs_are_enough():
    enough_bombs = [1 for key, value in made_bombs.items() if value['count'] > 2]
    if sum(enough_bombs) == 3:
        return True


bomb_effects = deque(int(x) for x in input().split(", "))
bomb_casings = deque(int(x) for x in input().split(", "))
made_bombs = {
    40: {'name': 'Datura Bombs', 'count': 0},
    60: {'name': 'Cherry Bombs', 'count': 0},
    120: {'name': 'Smoke Decoy Bombs', 'count': 0}
}
filled_bomb_pouch = False
while bomb_effects and bomb_casings:
    current_effect = bomb_effects[0]
    current_casing = bomb_casings[-1]
    bomb_power = current_effect + current_casing
    if bomb_power in made_bombs:
        made_bombs[bomb_power]['count'] += 1
        bomb_effects.popleft()
        bomb_casings.pop()
        if check_if_the_bombs_are_enough():
            filled_bomb_pouch = True
            break
        continue
    bomb_casings[-1] -= 5
if filled_bomb_pouch:
    print("Bene! You have successfully filled the bomb pouch!")
elif not filled_bomb_pouch:
    print("You don't have enough materials to fill the bomb pouch.")
if not bomb_effects:
    print("Bomb Effects: empty")
elif bomb_effects:
    print(f"Bomb Effects: {', '.join(str(x) for x in bomb_effects)}")
if not bomb_casings:
    print("Bomb Casings: empty")
elif bomb_casings:
    print(f"Bomb Casings: {', '.join(str(x) for x in bomb_casings)}")
for key, value in sorted(made_bombs.items(), key=lambda item: item[1]['name']):
    print(f"{value['name']}: {value['count']}")
