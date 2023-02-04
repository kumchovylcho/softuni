import os


def create_file(name: str):
    with open(name, 'w') as file:
        file.truncate()


def add_to_file(name_of_file: str, content: str):
    with open(name_of_file, 'a') as file:
        file.write(content + "\n")


def replace_occurrences_in_file(name_of_file: str, old_string: str, new_string: str):
    try:
        with open(name_of_file, 'r') as file:
            data = file.readlines()

        with open(name_of_file, 'w') as file:
            for line in data:
                file.write(line.replace(old_string, new_string))

    except FileNotFoundError:
        print("An error occurred")


def delete_file(name_of_file: str):
    try:
        os.remove(name_of_file)

    except FileNotFoundError:
        print("An error occurred")


task_executor = {
    "Create": create_file,
    "Add": add_to_file,
    "Replace": replace_occurrences_in_file,
    "Delete": delete_file,
}

command = input()
while command != "End":
    operation, file_name, *info = command.split("-")

    task_executor[operation](file_name, *info)

    command = input()