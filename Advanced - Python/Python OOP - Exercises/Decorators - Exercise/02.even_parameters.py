def even_parameters(function):
    def wrapper(*args):
        if all(isinstance(arg, int) and arg % 2 == 0 for arg in args):
            return function(*args)
        return "Please use only even numbers!"
    return wrapper
