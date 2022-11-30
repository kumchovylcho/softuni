def age_assignment(*args, **kwargs):
    result = []
    for name in sorted(args):
        for letter, age in kwargs.items():
            if letter == name[0]:
                result.append(f"{name} is {age} years old.")
    return '\n'.join(result)
