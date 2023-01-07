def type_check(type_to_check):  # gets the decorator parameter
    def decorator(function):    # receives *first_letter* function
        def wrapper(arg):       # receives the argument of *first_letter* function
            if isinstance(arg, type_to_check):
                return function(arg)
            return "Bad Type"
        return wrapper
    return decorator


@type_check(str)
def first_letter(word):
    return word[0]


print(first_letter('Hello World'))
print(first_letter(['Not', 'A', 'String']))