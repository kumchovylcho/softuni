first_number = int(input())
second_number = int(input())
counter = first_number
for letter in range(first_number, second_number + 1):
    current_letter = chr(counter)
    print(f"{current_letter}", end=" ")
    counter += 1
