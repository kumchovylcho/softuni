import os


def get_file_names_and_extensions(dir_name):
    result = {}
    for filename in os.listdir(dir_name):
        name, extension = filename.split(".")

        result["." + extension] = result.get("." + extension, []) + [f"- - - {name}.{extension}"]

    return result


def write_result_on_file(data_with_extensions: dict):
    with open('report.txt', 'w') as file:
        for key, value in sorted(data_with_extensions.items()):
            file.write(f"{key}\n")
            for filename in sorted(value):
                file.write(filename + "\n")


directory = input()

files_with_extensions = get_file_names_and_extensions(directory)
write_result_on_file(files_with_extensions)
