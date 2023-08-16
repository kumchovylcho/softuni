from collections import deque

monster_armors = deque(int(x) for x in input().split(","))
soldier_strikings = [int(x) for x in input().split(",")]
monsters_killed = 0

while monster_armors and soldier_strikings:
    armor = monster_armors.popleft()
    strike = soldier_strikings.pop()

    if strike >= armor:
        strike -= armor
        monsters_killed += 1

        if strike:
            if soldier_strikings:
                soldier_strikings[-1] += strike

            elif not soldier_strikings:
                soldier_strikings.append(strike)

    elif strike < armor:
        armor -= strike
        monster_armors.append(armor)


if not monster_armors:
    print("All monsters have been killed!")

if not soldier_strikings:
    print("The soldier has been defeated.")

print(f"Total monsters killed: {monsters_killed}")
