all_phones = input().split(", ")
command = input()
while command != "End":
    operation, *data = [item for item in command.split(" - ")]
    if operation == "Add":
        phone = data[0]
        if phone not in all_phones:
            all_phones.append(phone)

    elif operation == "Remove":
        phone = data[0]
        if phone in all_phones:
            all_phones.remove(phone)

    elif operation == "Bonus phone":
        old_phone, new_phone = [item for item in data[0].split(":")]
        if old_phone in all_phones:
            index_of_old_phone = all_phones.index(old_phone)
            all_phones.insert(index_of_old_phone + 1, new_phone)

    elif operation == "Last":
        phone = data[0]
        if phone in all_phones:
            index_of_phone = all_phones.index(phone)
            all_phones.append(all_phones.pop(index_of_phone))
    command = input()
print(', '.join(all_phones))
