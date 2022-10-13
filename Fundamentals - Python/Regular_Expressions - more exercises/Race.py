import re
names_of_participants = input().split(", ")
pattern_for_names = re.compile(r'(?P<name>[A-Za-z]+)')
pattern_for_digits = re.compile(r'(?P<digits>\d+)')
racers = {}
command = input()
while command != "end of race":
    match_name = pattern_for_names.finditer(command)
    match_digits = pattern_for_digits.finditer(command)
    name_of_current_person = ''.join([match['name'] for match in match_name])
    getting_all_digits = ''.join([match['digits'] for match in match_digits])
    kilometers_ran = sum(map(int, getting_all_digits))
    if name_of_current_person in names_of_participants:
        racers[name_of_current_person] = racers.get(name_of_current_person, 0) + kilometers_ran
    command = input()
for counter, (name, point) in enumerate(sorted(racers.items(), key=lambda points: -points[1]), 1):
    position = ''
    if counter == 1:
        position = "st"
    elif counter == 2:
        position = "nd"
    elif counter == 3:
        position = "rd"
    else:
        break
    print(f"{counter}{position} place: {name}")
