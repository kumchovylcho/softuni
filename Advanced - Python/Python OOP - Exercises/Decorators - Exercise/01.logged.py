def logged(function):
    def wrapper(*args):
        result = f"you called {function.__name__}({', '.join(str(x) for x in args)})\n" \
                 f"it returned {function(*args)}"
        return result
    return wrapper
