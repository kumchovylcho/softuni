number = int(input())


def is_perfect(num):
    result = num // 2
    while result > 2:
        result //= 2
    if result == 1:
        print("We have a perfect number!")
    elif result != 1:
        print("It's not so perfect.")


is_perfect(number)
