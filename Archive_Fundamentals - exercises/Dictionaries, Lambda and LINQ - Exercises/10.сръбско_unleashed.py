import re
musicians = {}
pattern = re.compile(r'(?P<name>.+)( )@(?P<place>[A-Za-z]+[ A-Za-z]*)\2(?P<price>\d+)\2(?P<count>\d+)')
singer_info = input()
while singer_info != "End":
    match = list(pattern.finditer(singer_info))
    if match:
        for matches in match:
            name, place, ticket_price, tickets_count = matches['name'], matches['place'],\
                                                       int(matches['price']), int(matches['count'])
        musicians[place] = musicians.get(place, {})
        musicians[place][name] = musicians[place].get(name, 0)
        musicians[place][name] += ticket_price * tickets_count
    singer_info = input()
for key in musicians:
    print(key)
    for name, value in sorted(musicians[key].items(), key=lambda x: -x[1]):
        print(f"#  {name} -> {musicians[key][name]}")

