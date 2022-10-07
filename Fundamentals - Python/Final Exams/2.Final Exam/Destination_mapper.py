import re
pattern = re.compile(r'([=|/])(?P<destination>[A-Z][A-Za-z]{2,})\1')
destinations = input()
matches = pattern.finditer(destinations)
travel_points = 0
valid_destinations = []
for match in matches:
    valid_destinations.append(match['destination'])
    travel_points += len(match['destination'])
print(f"Destinations: {', '.join(valid_destinations)}")
print(f"Travel Points: {travel_points}")