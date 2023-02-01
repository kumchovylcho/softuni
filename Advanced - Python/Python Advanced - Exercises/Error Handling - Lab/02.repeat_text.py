word = input()
try:
    repeat_times = int(input())

    result = word * repeat_times
    print(result)
except ValueError:
    print("Variable times must be an integer")


