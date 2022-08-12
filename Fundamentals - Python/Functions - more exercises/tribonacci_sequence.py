starting_number = int(input())
last_three = [1, 1]


def show_tribonacci(num):
    for number in range(1, num + 1):
        if number == 1 or number == 2:
            print(last_three[number - 1], end=" ")
            continue
        else:
            add_last_number = 0
            if len(last_three) > 2:
                add_last_number = last_three.pop(0)
        print(sum(last_three) + add_last_number, end=" ")
        last_three.append(sum(last_three) + add_last_number)


show_tribonacci(starting_number)