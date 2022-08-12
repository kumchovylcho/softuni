number = int(input())
if number > 1:
    for integer in range(2, number // 2):
        if number % integer == 0:
            print("False")
            break
    else:
        print("True")
