def forecast(*args):
    locations = {
        'Sunny': [],
        'Cloudy': [],
        'Rainy': []
    }
    for city, weather in sorted(args):
        locations[weather].append(city)
    result = []
    for key in locations:
        for value in locations[key]:
            result.append(f"{value} - {key}")
    return '\n'.join(result)
