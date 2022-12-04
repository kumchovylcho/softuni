import re
pattern = re.compile(r'!(?P<command>[A-Z][a-z]{2,})!:(?P<string>\[[A-Za-z]{8,}\])')
number_of_messages = int(input())
for _ in range(number_of_messages):
    current_message = input()
    matches = list(pattern.finditer(current_message))
    if matches:
        for match in matches:
            name = match['command']
            string = match['string']
            all_ascii_values = [ord(letter) for letter in string[1:-1]]
            print(f"{name}: {' '.join((str(x) for x in all_ascii_values))}")
    elif not matches:
        print("The message is invalid")


