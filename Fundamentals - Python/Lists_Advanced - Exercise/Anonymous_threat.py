from math import floor
words = input().split()             # NEED TO FIX THE DIVISION , THIS SOLUTION GETS 90/100


def merge(current_command, words):
    starting_index = int(current_command[1])
    ending_index = int(current_command[2])
    current_merge = []
    all_in_one_string = ""
    if starting_index < 0:
        starting_index = 0
    elif starting_index > len(words):
        starting_index = len(words) - 2
    if ending_index > len(words):
        ending_index = len(words)
    current_merge += words[starting_index:ending_index + 1]
    for word in current_merge:
        all_in_one_string += word
    del words[starting_index:ending_index + 1]
    words.insert(starting_index, all_in_one_string)


def divide(current_command, words):
    word_position = int(current_command[1])
    divide_into_pieces = int(current_command[2])
    if len(words[word_position]) < divide_into_pieces:
        divide_into_pieces = int(len(words[word_position]))
    elif divide_into_pieces == 0:
        divide_into_pieces = 1
    if len(words[word_position]) % divide_into_pieces == 0:
        how_many_substrings = int(len(words[word_position]) / divide_into_pieces)
        new_string = ""
        counter = 0
        for letter in words[word_position]:
            if counter == how_many_substrings:
                new_string += " "
                counter = 0
            new_string += letter
            counter += 1
        del words[word_position]
        words.insert(word_position, new_string)
    elif len(words[word_position]) % divide_into_pieces != 0:
        how_many_substrings = floor((len(words[word_position]) / divide_into_pieces))
        new_string = ""
        counter = 0
        counter_of_substrings = 0
        for letter in words[word_position]:
            if counter == how_many_substrings:
                new_string += " "
                counter = 0
                counter_of_substrings += 1
                if counter_of_substrings == divide_into_pieces - 1:
                    break
            new_string += letter
            counter += 1
        rest_of_the_word = len(new_string) - counter_of_substrings
        new_string += words[word_position][rest_of_the_word:]
        del words[word_position]
        words.insert(word_position, new_string)


command = input()
while command != "3:1":
    if "merge" in command:
        merge(command.split(), words)
    elif "divide" in command:
        divide(command.split(), words)
    command = input()

print(*words)
