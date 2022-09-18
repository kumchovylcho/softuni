name, volume, energy, sugar = input(), int(input()), int(input()), int(input())
print(f"{volume}ml {name}:\n{(volume * energy) / 100:.2f}kcal, {volume * (sugar / 100):.2f}g sugars")