text = input()
times_to_copy = int(input())


def new_text(string, times_multiplied):
    result = string * times_multiplied
    return result


print(new_text(text, times_to_copy))



# text, repeats = input(), int(input())
# repeat_string = lambda string, repeats: string * repeats
# result = repeat_string(text, repeats)
# print(result)


# print(input() * int(input()))
