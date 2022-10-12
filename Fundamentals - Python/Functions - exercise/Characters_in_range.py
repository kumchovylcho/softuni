def characters_in_between(start_index, end_index):
    start_index = ord(start_index) + 1
    end_index = ord(end_index)
    result = [chr(character) for character in range(start_index, end_index)]
    return result


starting_letter = input()
ending_letter = input()
# print(' '.join(characters_in_between(starting_letter, ending_letter)))
final_result = characters_in_between(starting_letter, ending_letter)
print(' '.join(final_result))


# start = input()
# end = input()
#
#
# def characters_in_between(start, end):
#     string = ""
#     for result in range(ord(start) + 1, ord(end)):
#         string += chr(result) + " "
#     return string
#
#
# print(characters_in_between(start, end))
