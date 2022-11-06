def add_information(count_of_pieces):
    for piece in range(count_of_pieces):
        piece, composer, key = input().split("|")
        pianist_collection[piece] = pianist_collection.get(piece, {'composer': composer, 'key': key})


def add_piece(piece, composer, key):
    if piece in pianist_collection:
        print(f"{piece} is already in the collection!")
    elif piece not in pianist_collection:
        pianist_collection[piece] = {'composer': composer, 'key': key}
        print(f"{piece} by {composer} in {key} added to the collection!")


def remove_piece(piece):
    if piece in pianist_collection:
        del pianist_collection[piece]
        print(f"Successfully removed {piece}!")
    elif piece not in pianist_collection:
        print(f"Invalid operation! {piece} does not exist in the collection.")


def change_key(piece, new_key):
    if piece in pianist_collection:
        pianist_collection[piece]['key'] = new_key
        print(f"Changed the key of {piece} to {new_key}!")
    elif piece not in pianist_collection:
        print(f"Invalid operation! {piece} does not exist in the collection.")


def main():
    command = input()
    while command != "Stop":
        operation, *info = command.split("|")
        pianist_operations[operation](*info)
        command = input()


def show_result():
    for piece, value in pianist_collection.items():
        print(f"{piece} -> Composer: {value['composer']}, Key: {value['key']}")


number_of_pieces = int(input())
pianist_collection = {}
pianist_operations = {
    'Add': add_piece,
    'Remove': remove_piece,
    'ChangeKey': change_key
}
add_information(number_of_pieces)
main()
show_result()


# def add_command(piece, composer, key):
#     if piece in piece_info:
#         print(f"{piece} is already in the collection!")
#     else:
#         piece_info[piece] = {'composer': composer, 'key': key}
#         print(f"{piece} by {composer} in {key} added to the collection!")
#
#
# def remove_command(piece):
#     if piece in piece_info:
#         del piece_info[piece]
#         print(f"Successfully removed {piece}!")
#     else:
#         print(f"Invalid operation! {piece} does not exist in the collection.")
#
#
# def change_key_command(piece, new_key):
#     if piece in piece_info:
#         piece_info[piece]['key'] = new_key
#         print(f"Changed the key of {piece} to {new_key}!")
#     else:
#         print(f"Invalid operation! {piece} does not exist in the collection.")
#
#
# number_of_pieces = int(input())
# piece_info = {}
#
# for _ in range(number_of_pieces):
#     piece, composer, key = input().split("|")
#     piece_info[piece] = {'composer': composer, 'key': key}
#
# command_line = input()
# while not command_line == 'Stop':
#     command, *info = [item for item in command_line.split("|")]
#     if command == 'Add':
#         add_command(*info)
#     elif command == 'Remove':
#         remove_command(*info)
#     elif command == 'ChangeKey':
#         change_key_command(*info)
#     command_line = input()
# for piece, info in piece_info.items():
#     print(f"{piece} -> Composer: {info['composer']}, Key: {info['key']}")


# number_of_pieces = int(input())
# pianist_collection = {}
#
# for pieces in range(number_of_pieces):
#     piece, composer, key = input().split("|")
#     pianist_collection[piece] = pianist_collection.get(composer, {})
#     pianist_collection[piece][composer] = pianist_collection[piece].get(composer, key)
#
# command = input()
# while command != "Stop":
#     command = command.split("|")
#     operation = command[0]
#     piece = command[1]
#
#     if operation == "Add":
#         composer, key = command[2], command[3]
#         if piece not in pianist_collection:
#             pianist_collection[piece] = {composer: key}
#             print(f"{piece} by {composer} in {key} added to the collection!")
#         else:
#             print(f"{piece} is already in the collection!")
#
#     elif operation == "Remove":
#         if piece in pianist_collection:
#             del pianist_collection[piece]
#             print(f"Successfully removed {piece}!")
#         else:
#             print(f"Invalid operation! {piece} does not exist in the collection.")
#
#     elif operation == "ChangeKey":
#         new_key = command[2]
#         if piece in pianist_collection:
#             for current_key in pianist_collection:
#                 if current_key == piece:
#                     for compositor in pianist_collection[current_key]:
#                         pianist_collection[current_key][compositor] = new_key
#                         break
#             print(f"Changed the key of {piece} to {new_key}!")
#         else:
#             print(f"Invalid operation! {piece} does not exist in the collection.")
#     command = input()
#
# for keys in pianist_collection:
#     for composers in pianist_collection[keys]:
#         print(f"{keys} -> Composer: {composers}, Key: {pianist_collection[keys][composers]}")
