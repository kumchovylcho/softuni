force_book = {}

command = input()
while command != "Lumpawaroo":
    if "|" in command:
        command = command.split(" | ")
        side, user = command[0], command[1]
        force_book[side] = force_book.get(side, [])
        no_user = True
        for key in force_book:
            if user in force_book[key]:
                no_user = False
                break
        if no_user:
            force_book[side].append(user)

    elif "->" in command:
        command = command.split(" -> ")
        user, side = command[0], command[1]

        for key in force_book:
            if user in force_book[key]:
                force_book[key].remove(user)
        force_book[side] = force_book.get(side, [])
        force_book[side].append(user)
        print(f"{user} joins the {side} side!")

    command = input()

for side in force_book:
    if force_book[side]:
        print(f"Side: {side}, Members: {len(force_book[side])}")
        for names in range(len(force_book[side])):
            print(f"! {force_book[side][names]}")



# force_command = input()
#
# force_book = {}
#
#
# def force_side(side_, user_):
#     for key in force_book:
#         if user_ in force_book[key]:
#             return
#     force_book[side_] = force_book.get(side_, {})
#     force_book[side_][user_] = force_book.get(side_)
#
#
# def force_change(user_, side_):
#     for key in force_book:
#         if user_ in force_book[key]:
#             del force_book[key][user_]
#             break
#     force_book[side_] = force_book.get(side_, {})
#     force_book[side_][user_] = force_book.get(side_)
#     print(f"{user_} joins the {side_} side!")
#
#
# while force_command != "Lumpawaroo":
#
#     if " | " in force_command:
#         force_command = force_command.split(" | ")
#         force_side(str(force_command[0]), str(force_command[-1]))
#     elif " -> " in force_command:
#         force_command = force_command.split(" -> ")
#         force_change(str(force_command[0]), str(force_command[-1]))
#     force_command = input()
#
# for side in force_book:
#     if force_book[side]:
#         print(f"Side: {side}, Members: {len(force_book[side])}")
#         for name in force_book[side]:
#             print(f"! {name}")
