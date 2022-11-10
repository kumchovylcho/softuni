clients = []
client_name = input()
while client_name != "End":
    if client_name == "Paid":
        print('\n'.join(clients))
        clients = []
        client_name = input()
        continue
    clients.append(client_name)
    client_name = input()
print(f"{len(clients)} people remaining.")

