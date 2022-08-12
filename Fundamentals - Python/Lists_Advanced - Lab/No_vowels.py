text = input()
vowels = "aoueiAOUEI"


def no_vowels(string):
    result = ""
    for letter in string:
        if letter in vowels:
            continue
        elif letter not in vowels:
            result += letter
    return result


print(no_vowels(text))
