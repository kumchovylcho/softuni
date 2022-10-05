words = input().split()


def merge(start_index, end_index, words):
    current_merge = []
    all_in_one_string = ""
    if start_index < 0:
        start_index = 0
    elif start_index > len(words):
        start_index = len(words) - 2
    if end_index > len(words):
        end_index = len(words) - 1
    current_merge += words[start_index:end_index + 1]
    for word in current_merge:
        all_in_one_string += word
    del words[start_index:end_index + 1]
    words.insert(start_index, all_in_one_string)


def divide(divide_index, how_many_pieces, words):
    how_long = len(words[divide_index])
    space_between = how_long // how_many_pieces
    string_to_change = words.pop(divide_index)
    result_ = []
    for x in range(how_many_pieces - 1):
        result_.append(string_to_change[:space_between])
        string_to_change = string_to_change[space_between:]
    result_.append(string_to_change)
    for x in result_[::-1]:
        words.insert(divide_index, x)


command = input()
while command != "3:1":
    command = command.split()
    operation = command[0]
    if operation == "merge":
        merge(int(command[1]), int(command[2]), words)
    elif operation == "divide":
        divide(int(command[1]), int(command[2]), words)
    command = input()

print(*words)
