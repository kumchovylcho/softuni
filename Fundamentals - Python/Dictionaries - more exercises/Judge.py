users_info = {
    'individuals': {},
    'contests': {}
}
contest = input()
while contest != "no more time":
    username, course, points = [int(name) if name.isdigit() else name for name in contest.split(" -> ")]
    users_info['contests'][course] = users_info['contests'].get(course, {})
    users_info['contests'][course][username] = users_info['contests'][course].get(username, 0)
    if users_info['contests'][course][username] < points:
        users_info['contests'][course][username] = points
    contest = input()
for exams in users_info['contests']:
    for names in users_info['contests'][exams]:
        users_info['individuals'][names] = users_info['individuals'].get(names, 0) + users_info['contests'][exams][names]

for submission in users_info['contests']:
    print(f"{submission}: {len(users_info['contests'][submission])} participants")
    for position, (name, points) in enumerate(
            sorted(users_info['contests'][submission].items(), key=lambda item: (-item[1], item[0])), 1):
        print(f"{position}. {name} <::> {points}")
print("Individual standings:")
for position, (name, points) in enumerate(
        sorted(users_info['individuals'].items(), key=lambda item: (-item[1], item[0])), 1):
    print(f"{position}. {name} -> {points}")
