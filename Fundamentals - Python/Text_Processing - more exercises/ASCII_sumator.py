starter_range = ord(input())
end_range = ord(input())
string = input()
total = 0

for character in string:
    if starter_range < ord(character) < end_range:
        total += ord(character)

print(total)