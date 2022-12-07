def start_spring(**kwargs):
    convert = {}
    for value, key in kwargs.items():
        convert[key] = convert.get(key, []) + [value]
    output = ""
    for key, value in sorted(convert.items(), key=lambda x: (-len(x[1]), x[0])):
        output += f"{key}:\n"
        for items in sorted(value):
            output += f"-{items}\n"
    return output
