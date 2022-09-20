first_letter, final_letter, banned_letter = ord(input()), ord(input()), ord(input())

for first in range(first_letter, final_letter + 1):
    for second in range(first_letter, final_letter + 1):
        for third in range(first_letter, final_letter + 1):
            if banned_letter == first or banned_letter == second or banned_letter == third:
                continue
            else:
                print(f"{chr(first)}{chr(second)}{chr(third)}", end=" ")
