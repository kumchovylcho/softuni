def calculate(command: str, calculation: str) -> int | str:
    operations = {
        "int": lambda number: int(number) * 2,
        "real": lambda number: f"{float(number) * 1.5:.2f}",
        "string": lambda value: f"${value}$"
    }

    # returns empty string if wrong command is provided
    return operations.get(command, lambda x: "")(calculation)


print(calculate(input(), input()))



##############################################################


# command = input()
# to_process = input()
#
#
# def calculate(command, calculation):
#     result = ""
#     if command == "int":
#         result = f"{int(calculation) * 2:.0f}"
#     elif command == "real":
#         result = f"{float(calculation) * 1.5:.2f}"
#     elif command == "string":
#         result = "$" + calculation + "$"
#     return result
#
#
# print(calculate(command, to_process))
