def get_brackets_only(values: list[str]) -> list[str]:
    return [bracket for bracket in values if bracket == "(" or bracket == ")"]


def match_pair(open_b: str, close_b: str) -> bool:
    return open_b + close_b == "()"


def are_brackets_balanced(brackets: list[str]) -> bool:
    while brackets:
        left_bracket = brackets.pop(0)
        right_bracket = None
        if brackets:
            right_bracket = brackets.pop(0)

        if right_bracket is None:
            return False

        if not match_pair(left_bracket, right_bracket):
            return False

    return True


def main(amount_of_inputs: int) -> None:
    brackets_only = get_brackets_only(
        [input() for _ in range(amount_of_inputs)]
    )
    balanced = are_brackets_balanced(brackets_only)
    if balanced:
        print("BALANCED")
    else:
        print("UNBALANCED")


main(int(input()))


###############################################
# number_of_lines = int(input())
# brackets = 0
# for bracket in range(1, number_of_lines + 1):
#     current_symbol = input()
#     if current_symbol == "(":
#         brackets += 1
#     elif current_symbol == ")":
#         brackets -= 1
#     if brackets != 0 and brackets != 1:
#         print("UNBALANCED")
#         break
# else:
#     print("BALANCED")
