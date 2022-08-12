start = input()
end = input()


def characters_in_between(start, end):
    string = ""
    for result in range(ord(start) + 1, ord(end)):
        string += chr(result) + " "
    return string


print(characters_in_between(start, end))
