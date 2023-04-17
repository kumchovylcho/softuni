last_sector = ord(input())
rows = int(input())
odd_spots = int(input())

all_spots = 0

for sector in range(65, last_sector + 1):
    for row in range(1, rows + 1):
        extra_spots = odd_spots + 2 if row % 2 == 0 else odd_spots

        for letter in range(97, 97 + extra_spots):
            print(f"{chr(sector)}{row}{chr(letter)}")
            all_spots += 1

    rows += 1

print(all_spots)