def even_odd_filter(**kwargs):
    filtered = {}
    for command in kwargs:
        filtered[command] = filtered.get(command, [])
        if command == 'even':
            filtered[command] = [digit for digit in kwargs[command] if digit % 2 == 0]
        elif command == 'odd':
            filtered[command] = [digit for digit in kwargs[command] if digit % 2 != 0]
    sorted_items = {}
    for operation, values in sorted(filtered.items(), key=lambda item: -len(item[1])):
        sorted_items[operation] = values
    return sorted_items


print(even_odd_filter(
    odd=[1, 2, 3, 4, 10, 5],
    even=[3, 4, 5, 7, 10, 2, 5, 5, 2],
))
