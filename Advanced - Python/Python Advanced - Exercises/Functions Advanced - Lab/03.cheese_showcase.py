def sorting_cheeses(**kwargs):
    sorted_info = {}
    result = ""
    for name, value in sorted(kwargs.items(), key=lambda item: (-len(item[1]), item[0])):
        sorted_info[name] = sorted_info.get(name, []) + [str(x) for x in sorted(value, reverse=True)]
    for name in sorted_info:
        result += f"{name}\n"
        for price in sorted_info[name]:
            result += f"{price}\n"
    return result
