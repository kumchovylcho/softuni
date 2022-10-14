import re
pattern = re.compile(r'@(?P<planet>[A-Za-z]+)([^\@\,\-\!\:\>]*)'
                     r':(?P<population>[0-9]+)([^\@\,\-\!\:\>]*)'
                     r'!(?P<action>[A|D])!([^\@\,\-\!\:\>]*)'
                     r'->(?P<soldiers>[0-9]+)')
letters_to_count = "starSTAR"
attacked_planets, destroyed_planets = [], []
how_many_encrypted_strings = int(input())
for string in range(how_many_encrypted_strings):
    current_string = input()
    how_many_found = [character for character in current_string if character in letters_to_count]
    decrypted_string = ''.join([chr(ord(character) - len(how_many_found)) for character in current_string])
    matches = pattern.finditer(decrypted_string)
    for match in matches:
        if match['action'] == "A":
            attacked_planets.append(match['planet'])
        elif match['action'] == "D":
            destroyed_planets.append(match['planet'])
print(f"Attacked planets: {len(attacked_planets)}")
if attacked_planets:
    for planet in sorted(attacked_planets):
        print(f"-> {planet}")
print(f"Destroyed planets: {len(destroyed_planets)}")
if destroyed_planets:
    for planet in sorted(destroyed_planets):
        print(f"-> {planet}")

