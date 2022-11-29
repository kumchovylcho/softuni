import re
messages = int(input())
found_planets = []
allowed_characters = "SsTtAaRr"
for _ in range(messages):
    current_message = input()
    counter = 0
    for letter in allowed_characters:
        counter += current_message.count(letter)
    found_planets.append(''.join(chr(ord(x) - counter) for x in current_message))
planet_pattern = re.compile(r'@(?P<planet>[A-Za-z]+)[0-9]*[^@|\-|!|:|>]*'
                            r':(?P<population>\d+)[^@|\-|!|:|>]*'
                            r'!(?P<type>A|D)![^@|\-|!|:|>]*'
                            r'->(?P<soldiers>\d+)')
attacked_planets, destroyed_planets = [], []
for planet in found_planets:
    result = list(planet_pattern.finditer(planet))
    for check in result:
        if check['type'] == "A":
            attacked_planets.append(check['planet'])
        elif check['type'] == "D":
            destroyed_planets.append(check['planet'])
print(f"Attacked planets: {len(attacked_planets)}")
[print(f"-> {x}") for x in sorted(attacked_planets)]
print(f"Destroyed planets: {len(destroyed_planets)}")
[print(f"-> {x}") for x in sorted(destroyed_planets)]


# import re
# pattern = re.compile(r'@(?P<planet>[A-Za-z]+)([^\@\,\-\!\:\>]*)'
#                      r':(?P<population>[0-9]+)([^\@\,\-\!\:\>]*)'
#                      r'!(?P<action>[A|D])!([^\@\,\-\!\:\>]*)'
#                      r'->(?P<soldiers>[0-9]+)')
# letters_to_count = "starSTAR"
# attacked_planets, destroyed_planets = [], []
# how_many_encrypted_strings = int(input())
# for string in range(how_many_encrypted_strings):
#     current_string = input()
#     how_many_found = [character for character in current_string if character in letters_to_count]
#     decrypted_string = ''.join([chr(ord(character) - len(how_many_found)) for character in current_string])
#     matches = pattern.finditer(decrypted_string)
#     for match in matches:
#         if match['action'] == "A":
#             attacked_planets.append(match['planet'])
#         elif match['action'] == "D":
#             destroyed_planets.append(match['planet'])
# print(f"Attacked planets: {len(attacked_planets)}")
# if attacked_planets:
#     for planet in sorted(attacked_planets):
#         print(f"-> {planet}")
# print(f"Destroyed planets: {len(destroyed_planets)}")
# if destroyed_planets:
#     for planet in sorted(destroyed_planets):
#         print(f"-> {planet}")

