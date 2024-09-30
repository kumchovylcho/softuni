def valid_indexes(valid_index_for: str, *indexes) -> bool:
    for index in indexes:
        if not 0 <= index < len(valid_index_for):
            return False
    return True


def main(username: str) -> None:
    command = input()
    while command != END_OF_COMMANDS:
        operation, *args = command.split()

        if operation == "Letters":
            cast_to = args[0]
            username = {"Lower": username.lower, "Upper": username.upper}[cast_to]()
            print(username)
        elif operation == "Reverse":
            start, end = [int(x) for x in args]
            if not valid_indexes(username, start, end):
                command = input()
                continue

            reversed_substring = username[start:end + 1][::-1]
            print(reversed_substring)
        elif operation == "Substring":
            substring = args[0]
            if substring not in username:
                print(f"The username {username} doesn't contain {substring}.")
                command = input()
                continue

            username = username.replace(substring, "", 1)
            print(username)
        elif operation == "Replace":
            replace_with = args[0]
            username = username.replace(replace_with, "-")
            print(username)
        elif operation == "IsValid":
            character = args[0]
            if character not in username:
                print(f"{character} must be contained in your username.")
                command = input()
                continue

            print("Valid username.")

        command = input()


END_OF_COMMANDS = "Registration"
main(input())