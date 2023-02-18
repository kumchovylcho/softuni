from collections import deque

textiles = deque(int(x) for x in input().split())
medicaments = [int(x) for x in input().split()]

items = {
    30: {'name': 'Patch', 'crafted': 0},
    40: {'name': 'Bandage', 'crafted': 0},
    100: {'name': 'MedKit', 'crafted': 0},
}

while textiles and medicaments:
    textile = textiles.popleft()
    medicament = medicaments.pop()

    sum = textile + medicament
    if sum in items:
        items[sum]['crafted'] += 1
        continue

    if sum > 100:
        items[100]['crafted'] += 1

        sum -= 100
        if medicaments:
            medicaments[-1] += sum
        continue

    medicaments.append(medicament + 10)


if not textiles and not medicaments:
    print("Textiles and medicaments are both empty.")
elif not textiles:
    print("Textiles are empty.")
elif not medicaments:
    print("Medicaments are empty.")

for value in sorted(items.values(), key=lambda x: (-x['crafted'], x['name'])):
    if value['crafted']:
        print(f"{value['name']} - {value['crafted']}")

if medicaments:
    print(f"Medicaments left: {', '.join([str(x) for x in medicaments][::-1])}")
if textiles:
    print(f"Textiles left: {', '.join(str(x) for x in textiles)}")
