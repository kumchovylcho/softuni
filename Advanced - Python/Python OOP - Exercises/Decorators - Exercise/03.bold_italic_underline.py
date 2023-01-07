def make_bold(function):
    def wrapper(*args):
        return f"<b>{function(*args)}</b>"
    return wrapper


def make_italic(function):
    def wrapper(*args):
        return f"<i>{function(*args)}</i>"
    return wrapper


def make_underline(function):
    def wrapper(*args):
        return f"<u>{function(*args)}</u>"
    return wrapper


@make_bold          # 1 -> 3
@make_italic        # 2 -> 2
@make_underline     # 3 -> 1
def greet_all(*args):
    return f"Hello, {', '.join(args)}"


print(greet_all("Peter", "George"))