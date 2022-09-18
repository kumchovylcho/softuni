stable_number, counter = int(input()), int(input())
if counter <= 10:
    for number in range(counter, 11):
        print(f"{stable_number} X {number} = {stable_number * number}")
elif counter > 10:
    print(f"{stable_number} X {counter} = {stable_number * counter}")