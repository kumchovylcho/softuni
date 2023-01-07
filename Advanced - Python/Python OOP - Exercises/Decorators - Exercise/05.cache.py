def cache(func):
    def wrapper(number):
        key = number
        if key not in wrapper.log:
            wrapper.log[key] = func(number)
        return wrapper.log[key]
    wrapper.log = {}
    return wrapper


@cache
def fibonacci(n):
    if n < 2:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)


print(fibonacci(3))
print(fibonacci.log)