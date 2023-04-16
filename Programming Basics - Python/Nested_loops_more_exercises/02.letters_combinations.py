start_letter = ord(input())
end_letter = ord(input())
avoid_letter = ord(input())

combinations = 0

for f_letter in range(start_letter, end_letter + 1):
    for s_letter in range(start_letter, end_letter + 1):
        for t_letter in range(start_letter, end_letter + 1):
            if any(x == avoid_letter for x in (f_letter, s_letter, t_letter)):
                continue

            print(f"{chr(f_letter)}{chr(s_letter)}{chr(t_letter)}", end=' ')
            combinations += 1

print(combinations)