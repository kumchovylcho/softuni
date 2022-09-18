name = input()
current_hp, max_hp, current_energy, max_energy = [int(input()) for _ in range(4)]
print(f"Name: {name}")
print(f"Health: |{current_hp * '|'}{(max_hp - current_hp) * '.'}|")
print(f"Energy: |{current_energy * '|'}{(max_energy - current_energy) * '.'}|")