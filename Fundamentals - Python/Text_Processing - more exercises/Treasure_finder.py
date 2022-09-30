keys = input().split()
index_of_keys = 0

all_results = []

string = input()
while string != "find":
    result = ''
    for character in string:
        if index_of_keys >= len(keys):
            index_of_keys = 0
        result += chr(ord(character) - int(keys[index_of_keys]))
        index_of_keys += 1

    all_results.append(result)
    result, index_of_keys = '', 0
    string = input()

for location in all_results:
    start_index_material = location.index("&") + 1
    end_index_material = location.index("&", start_index_material + 1)
    start_coordinates, end_coordinates = location.index("<") + 1, location.index(">")
    print(f"Found {location[start_index_material:end_index_material]} at {location[start_coordinates:end_coordinates]}")
