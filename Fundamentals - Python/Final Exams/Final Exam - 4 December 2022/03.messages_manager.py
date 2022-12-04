possible_messages = int(input())
users_manager = {}
command = input()
while command != "Statistics":
    command = command.split("=")
    operation = command[0]
    if operation == "Add":
        username, sent, received = command[1], int(command[2]), int(command[3])
        users_manager[username] = users_manager.get(username, {'sent': sent, 'received': received})

    elif operation == "Message":
        sender, receiver = command[1], command[2]
        if sender in users_manager and receiver in users_manager:
            users_manager[sender]['sent'] += 1
            users_manager[receiver]['received'] += 1
            if users_manager[sender]['sent'] + users_manager[sender]['received'] >= possible_messages:
                del users_manager[sender]
                print(f"{sender} reached the capacity!")
            if users_manager[receiver]['received'] + users_manager[receiver]['sent'] >= possible_messages:
                del users_manager[receiver]
                print(f"{receiver} reached the capacity!")

    elif operation == "Empty":
        username = command[1]
        if username == "All":
            users_manager = {}
        elif username in users_manager:
            del users_manager[username]
    command = input()

print(f"Users count: {len(users_manager)}")
for user, messages in users_manager.items():
    print(f"{user} - {messages['sent'] + messages['received']}")