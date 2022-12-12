import re
pattern = re.compile(r'(?P<name>.+)=(?P<length>\d+[^.,:])<<(?P<code>.+)')
string = input()
while string != "Last note":
    matches = pattern.finditer(string)
    for match in matches:
        unwanted_symbols = '.,:'
        found_name = match['name']
        found_code = match['code']
        check_symbols = [letter for letter in found_name if letter in unwanted_symbols]
        check_symbols_in_code = [letter for letter in found_code if letter in unwanted_symbols]
        if not check_symbols and not check_symbols_in_code and int(match['length']) == len(found_code):
            name = ''.join([letter for letter in found_name if letter.isalpha() or letter.isdigit()])
            print(f"Coordinates found! {name} -> {found_code}")
        break
    else:
        print("Nothing found!")
    string = input()

