def contain(substring, main_text):
    if str(substring) in main_text:
        print(f"{main_text} contains {substring}")
        return
    print("Substring not found!")


def flip(upper_or_lower, start_index, end_index, main_text):
    if upper_or_lower == 'Upper':
        main_text = main_text[:start_index] + main_text[start_index:end_index].upper() + \
                    main_text[end_index:]
    elif upper_or_lower == 'Lower':
        main_text = main_text[:start_index] + main_text[start_index:end_index].lower() + \
                    main_text[end_index:]
    return main_text


def slice_string(start_index, end_index, main_text):
    main_text = main_text[:start_index] + main_text[end_index:]
    return main_text


text = input()
command = input()
while command != "Generate":
    instructions, *data = [int(x) if x.isdigit() else x for x in command.split(">>>")]
    if instructions == "Contains":
        contain(*data, text)
    elif instructions == "Flip":
        text = flip(*data, text)
    elif instructions == "Slice":
        text = slice_string(*data, text)
    if instructions != "Contains":
        print(text)
    command = input()
print(f"Your activation key is: {text}")


# activation_key = input()
#
# command = input()
# while command != "Generate":
#     command = command.split(">>>")
#
#     if command[0] == "Contains":
#         substring = command[1]
#         if substring in activation_key:
#             print(f"{activation_key} contains {substring}")
#
#         elif substring not in activation_key:
#             print("Substring not found!")
#
#     elif command[0] == "Flip":
#         upper_or_lower_letters = command[1]
#         start_index = int(command[2])
#         end_index = int(command[3])
#         if upper_or_lower_letters == "Upper":
#             activation_key = activation_key[:start_index] + activation_key[start_index:end_index].upper() \
#                              + activation_key[end_index:]
#
#         elif upper_or_lower_letters == "Lower":
#             activation_key = activation_key[:start_index] + activation_key[start_index:end_index].lower() \
#                              + activation_key[end_index:]
#
#     elif command[0] == "Slice":
#         start_index = int(command[1])
#         end_index = int(command[2])
#         activation_key = activation_key[:start_index] + activation_key[end_index:]
#
#     if command[0] != "Contains":
#         print(activation_key)
#
#     command = input()
#
# print(f"Your activation key is: {activation_key}")
