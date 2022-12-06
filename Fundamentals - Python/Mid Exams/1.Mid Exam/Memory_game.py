elements = input().split()
number_of_moves = 1
integers = input()
while integers != "end":
    first_index, second_index = [int(x) for x in integers.split()]
    if first_index == second_index or \
            first_index >= len(elements) or first_index < 0 or \
            second_index >= len(elements) or second_index < 0:
        middle = len(elements) // 2
        elements.insert(middle, f"-{number_of_moves}a")
        elements.insert(middle, f"-{number_of_moves}a")
        print("Invalid input! Adding additional elements to the board")
    elif first_index != second_index and elements[first_index] == elements[second_index]:
        removed_element = elements[first_index]
        elements.remove(removed_element)
        elements.remove(removed_element)
        print(f"Congrats! You have found matching elements - {removed_element}!")
    elif elements[first_index] != elements[second_index]:
        print("Try again!")
    if not elements:
        print(f"You have won in {number_of_moves} turns!")
        break
    number_of_moves += 1
    integers = input()
if elements:
    print("Sorry you lose :(")
    print(' '.join(elements))


# def out_of_bound_check(main_list, index_one, index_two):
#     if 0 <= index_one < len(main_list) \
#             and 0 <= index_two < len(main_list):
#         return True
#     return False
#
#
# def add_matching_elements(main_list, current_move):
#     middle_of_list = len(main_list) // 2
#     main_list.insert(middle_of_list, f"-{current_move}a"), main_list.insert(middle_of_list, f"-{current_move}a")
#     return main_list
#
#
# def remove_matching_elements(main_list, index_one, index_two):
#     index_of_rightest_item = 0
#     item_to_remove = main_list.index(main_list[index_one])
#     for rightest_index in range(len(main_list) - 1, -1, -1):
#         if main_list[rightest_index] == main_list[index_two]:
#             index_of_rightest_item = rightest_index
#             break
#     main_list.pop(index_of_rightest_item)
#     main_list.pop(item_to_remove)
#     return main_list
#
#
# number_of_moves = 0
# all_elements = input().split()
# indexes = input()
# while indexes != "end":
#     number_of_moves += 1
#     first_index, second_index = [int(index) for index in indexes.split()]
#     if out_of_bound_check(all_elements, first_index, second_index) \
#             and all_elements[first_index] != all_elements[second_index]:
#         print("Try again!")
#     elif first_index != second_index \
#             and out_of_bound_check(all_elements, first_index, second_index) \
#             and all_elements[first_index] == all_elements[second_index]:
#         print(f"Congrats! You have found matching elements - {all_elements[first_index]}!")
#         all_elements = remove_matching_elements(all_elements, first_index, second_index)
#     elif not out_of_bound_check(all_elements, first_index, second_index) or first_index == second_index:
#         all_elements = add_matching_elements(all_elements, number_of_moves)
#         print("Invalid input! Adding additional elements to the board")
#
#     if not all_elements:
#         break
#     indexes = input()
# if not all_elements:
#     print(f"You have won in {number_of_moves} turns!")
# elif all_elements:
#     print("Sorry you lose :(")
#     print(' '.join(all_elements))


# elements = input().split()
# moves = 0
#
#
# def cheating_detection():
#     middle = len(elements) // 2
#     elements.insert(middle, f"-{moves}a"), elements.insert(middle, f"-{moves}a")
#     print("Invalid input! Adding additional elements to the board")
#
#
# def remove_matching_elements(index1):
#     global elements
#     print(f"Congrats! You have found matching elements - {elements[index1]}!")
#     elements = [item for item in elements if item != elements[index1]]
#
#
# indexes = input()
# while indexes != "end":
#     moves += 1
#     indexes = indexes.split()
#     first_index = int(indexes[0])
#     second_index = int(indexes[1])
#     out_of_bound_checker = [index for index in indexes if 0 > int(index) or int(index) >= len(elements)]
#     if out_of_bound_checker or first_index == second_index:
#         cheating_detection()
#     elif elements[first_index] == elements[second_index]:
#         remove_matching_elements(first_index)
#     elif elements[first_index] != elements[second_index]:
#         print("Try again!")
#     if not len(elements):
#         print(f"You have won in {moves} turns!")
#         break
#     indexes = input()
#
# if indexes == "end" and len(elements):
#     print("Sorry you lose :(")
#     print(*elements, end=" ")
