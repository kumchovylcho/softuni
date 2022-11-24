initial_health = int(input())
max_health = initial_health
immune_system = {}
is_defeated = False
virus = input()
while virus != "end":
    if virus not in immune_system:
        virus_strength = sum([ord(letter) for letter in virus]) // 3
        time_to_defeat = virus_strength * len(virus)
        immune_system[virus] = {'strength': virus_strength, 'time': time_to_defeat}

    elif virus in immune_system:
        time_to_defeat = immune_system[virus]['time'] // 3

    print(f"Virus {virus}: {immune_system[virus]['strength']} => {time_to_defeat} seconds")
    if initial_health >= time_to_defeat:
        initial_health -= time_to_defeat
        print(f"{virus} defeated in {time_to_defeat // 60}m {time_to_defeat % 60}s.")
        print(f"Remaining health: {initial_health}")
        initial_health += int(0.2 * initial_health)
        if initial_health > max_health:
            initial_health = max_health
    elif initial_health < time_to_defeat:
        print("Immune System Defeated.")
        is_defeated = True
        break
    virus = input()

if not is_defeated:
    print(f"Final Health: {initial_health}")