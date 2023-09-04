def create_bar(percentage_fill: int):
    percentage_fill //= 10

    perc_symbols = "%" * percentage_fill
    dot_symbols = "." * (10 - len(perc_symbols))

    return f"[{perc_symbols}{dot_symbols}]"


def display_result(percentage_fill: int):
    result = []
    bar = create_bar(percentage_fill)

    if percentage_fill == 100:
        result.append("100% Complete!")
        result.append(bar)

    elif percentage_fill != 100:
        result.append(f"{percentage_fill}% {bar}")
        result.append("Still loading...")

    return "\n".join(result)


percentage = int(input())
print(display_result(percentage))



########################################################################


# percentage_loaded = int(input())
#
#
# def loading_bar(percentage):
#     percentage_symbols = percentage // 10
#     dot_symbols = 10 - percentage_symbols
#     bar = f"{percentage}% [{percentage_symbols * '%'}{dot_symbols * '.'}]"
#     if percentage in range(0, 100):
#         return f"{bar}\nStill loading..."
#     elif percentage == 100:
#         return f"100% Complete!\n[{percentage_symbols * '%'}]"
#
#
# result = loading_bar(percentage_loaded)
# print(result)


# def loading_bar(percentage):
#     percentage_symbols = percentage // 10
#     dot_symbols = 10 - percentage_symbols
#     bar = f"{percentage}% [{percentage_symbols * '%'}{dot_symbols * '.'}]"
#     if percentage in range(0, 100):
#         print(bar)
#         print("Still loading...")
#     elif percentage == 100:
#         print("100% Complete!")
#         print(f"[{percentage_symbols * '%'}]")
#
#
# percentage_loaded = int(input())
# loading_bar(percentage_loaded)
