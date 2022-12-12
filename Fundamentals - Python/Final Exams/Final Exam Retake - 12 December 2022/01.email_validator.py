email = input()
command = input()
while command != "Complete":
    command = command.split()
    task = command[0]
    if task == "Make":
        upper_or_lower = command[1]
        if upper_or_lower == "Lower":
            email = email[:].lower()
        elif upper_or_lower == "Upper":
            email = email[:].upper()
        print(email)
    elif task == "GetDomain":
        count = int(command[1])
        print(email[-count:])
    elif task == "GetUsername":
        if "@" in email:
            index = email.index("@")
            print(email[:index])
        elif "@" not in email:
            print(f"The email {email} doesn't contain the @ symbol.")
    elif task == "Replace":
        replacement_character = command[1]
        email = email.replace(replacement_character, "-")
        print(email)
    elif task == "Encrypt":
        values = [ord(letter) for letter in email]
        print(*values, sep=' ')
    command = input()