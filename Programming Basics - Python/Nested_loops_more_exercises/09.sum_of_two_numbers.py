start = int(input())
end = int(input())

magic_number = int(input())

combinations = 0
result = ''

for f in range(start, end + 1):
    for s in range(start, end + 1):
        combinations += 1

        if f + s == magic_number:
            result = f'({f} + {s} = {magic_number})'
            break

    if result:
        break


if result:
    print(f"Combination N:{combinations} {result}")

elif not result:
    print(f"{combinations} combinations - neither equals {magic_number}")