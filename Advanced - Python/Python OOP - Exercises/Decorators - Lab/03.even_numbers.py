from functools import wraps


def even_numbers(func):
    @wraps(func)
    def wrapper(numbers):
        return [num for num in numbers if num % 2 == 0]
    return wrapper


@even_numbers
def get_numbers(numbers):
    return numbers
