def team_lineup(*args):
    country_people = {}

    for player, country in args:
        country_people[country] = country_people.get(country, []) + [player]

    result = []
    for country, people in sorted(country_people.items(), key=lambda x: (-len(x[1]), x[0])):
        result.append(f"{country}:")

        for person in people:
            result.append(f"  -{person}")

    return "\n".join(result)