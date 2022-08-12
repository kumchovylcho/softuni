command = input()
to_process = input()


def calculate(command, calculation):
    result = ""
    if command == "int":
        result = f"{int(calculation) * 2:.0f}"
    elif command == "real":
        result = f"{float(calculation) * 1.5:.2f}"
    elif command == "string":
        result = "$" + calculation + "$"
    return result


print(calculate(command, to_process))
