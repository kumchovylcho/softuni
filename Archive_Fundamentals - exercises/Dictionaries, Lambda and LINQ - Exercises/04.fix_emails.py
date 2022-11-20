emails = {}
name = input()
while name != "stop":
    email = input()
    test = email[-2:]
    if email[-2:] not in "usuk":
        emails[name] = email
    name = input()
for key, value in emails.items():
    print(f"{key} -> {value}")
