text = input()
vowels = "aoueiAOUEI"
result = [letter for letter in text if letter not in vowels]
print(''.join(result))



# def no_vowels(string):
#     result = ""
#     for letter in string:
#         if letter not in vowels:
#             result += letter
#     return result
#
#
# text = input()
# vowels = "aoueiAOUEI"
# print(no_vowels(text))
