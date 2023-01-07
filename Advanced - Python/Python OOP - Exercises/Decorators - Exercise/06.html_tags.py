def tags(tag):
    def decorator(function):
        def wrapper(*args):
            return f"<{tag}>{function(*args)}</{tag}>"
        return wrapper
    return decorator


@tags('h1')
def to_upper(text):
    return text.upper()


print(to_upper('hello'))