elements = input().split()
moves = 0


def cheating_detection():
    middle = len(elements) // 2
    elements.insert(middle, f"-{moves}a"), elements.insert(middle, f"-{moves}a")
    print("Invalid input! Adding additional elements to the board")


def remove_matching_elements(index1):
    global elements
    print(f"Congrats! You have found matching elements - {elements[index1]}!")
    elements = [item for item in elements if item != elements[index1]]


indexes = input()
while indexes != "end":
    moves += 1
    indexes = indexes.split()
    first_index = int(indexes[0])
    second_index = int(indexes[1])
    out_of_bound_checker = [index for index in indexes if 0 > int(index) or int(index) >= len(elements)]
    if out_of_bound_checker or first_index == second_index:
        cheating_detection()
    elif elements[first_index] == elements[second_index]:
        remove_matching_elements(first_index)
    elif elements[first_index] != elements[second_index]:
        print("Try again!")
    if not len(elements):
        print(f"You have won in {moves} turns!")
        break
    indexes = input()

if indexes == "end" and len(elements):
    print("Sorry you lose :(")
    print(*elements, end=" ")
