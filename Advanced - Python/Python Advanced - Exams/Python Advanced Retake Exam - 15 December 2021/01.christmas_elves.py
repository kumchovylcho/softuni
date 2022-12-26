from collections import deque
elf_energy = deque(int(x) for x in input().split())
materials = deque(int(x) for x in input().split())
toys_counter = 0
day_counter = 0
total_energy = 0
while elf_energy and materials:
    while elf_energy[0] < 5:
        elf_energy.popleft()
        if len(elf_energy) == 0:
            break
    if len(elf_energy) == 0:
        break
    day_counter += 1
    if day_counter % 3 != 0:
        if elf_energy[0] >= materials[-1]:
            if day_counter % 5 == 0:
                elf_energy[0] -= materials[-1]
            else:
                elf_energy[0] -= materials[-1] - 1
                toys_counter += 1
            total_energy += materials[-1]
            materials.pop()
            elf_energy.append(elf_energy.popleft())
        else:
            elf_energy[0] *= 2
            elf_energy.append(elf_energy.popleft())
    elif day_counter % 3 == 0:
        if elf_energy[0] >= materials[-1] * 2:
            if day_counter % 5 == 0:
                elf_energy[0] -= materials[-1] * 2
            else:
                elf_energy[0] -= materials[-1] * 2 - 1
                toys_counter += 2
            total_energy += materials[-1] * 2
            materials.pop()
            elf_energy.append(elf_energy.popleft())
        else:
            elf_energy[0] *= 2
            elf_energy.append(elf_energy.popleft())
print(f"Toys: {toys_counter}")
print(f"Energy: {total_energy}")
if len(elf_energy) > 0:
    print(f"Elves left: {', '.join(str(x) for x in elf_energy)}")
if len(materials) > 0:
    print(f"Boxes left: {', '.join(str(x) for x in materials)}")
