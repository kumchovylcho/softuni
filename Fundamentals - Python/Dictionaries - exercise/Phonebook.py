phonebook = dict()

phone_numbers = input()
while "-" in phone_numbers:
    phone_numbers = phone_numbers.split("-")
    person_name = phone_numbers[0]
    person_phone_number = phone_numbers[1]

    phonebook[person_name] = person_phone_number

    phone_numbers = input()


for name in range(int(phone_numbers)):
    wanted_name = input()
    if wanted_name in phonebook:
        print(f"{wanted_name} -> {phonebook[wanted_name]}")
    elif wanted_name not in phonebook:
        print(f"Contact {wanted_name} does not exist.")