from re import findall


class NameTooShortError(Exception):
    pass


class MustContainAtSymbolError(Exception):
    pass


class InvalidDomainError(Exception):
    pass


valid_domains = (".com", ".bg", ".net", ".org")
MIN_LENGTH = 4

email = input()
while email:
    if "@" not in email:
        """
        this statement is first, so we guarantee that we have @ symbol below
        """
        raise MustContainAtSymbolError("Email must contain @")

    if len(email.split("@")[0]) < MIN_LENGTH:
        """
        it is guaranteed that we have @ symbol and if there isn't any letter before the @ symbol,
        then index 0 will be empty
        """
        raise NameTooShortError("Name must be more than 4 letters")

    find_domain = findall(r'\.+[a-z]+', email)
    if not find_domain or find_domain[-1] not in valid_domains:
        """
        checking if there is no match or,
        if there is a match but it is not valid domain, we throw an error
        """
        raise InvalidDomainError(f"you must enter valid domains - {', '.join(valid_domains)}")

    print("Email is valid")

    email = input()
