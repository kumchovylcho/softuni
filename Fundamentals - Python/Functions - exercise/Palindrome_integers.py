def palindrome_checker(all_numbers):
    result = [True if number == number[::-1] else False for number in all_numbers]
    return result
    # result = []
    # for number in all_numbers:
    #     if number == number[::-1]:
    #         result.append(True)
    #     else:
    #         result.append(False)
    # return result


numbers = input().split(", ")
final_result = palindrome_checker(numbers)
for boolean in final_result:
    print(boolean)



# def is_palindrome(number):
#     for num in number:
#         if num == num[::-1]:
#             print("True")
#         elif num != num[::-1]:
#             print("False")
#
#
# numbers = input().split(", ")
# is_palindrome(numbers)





# all_numbers = input().split(", ")
#
#
# def is_palindrome(number):
#     result = ""
#     for num in number:
#         if num == num[::-1]:
#             result += f"True\n"
#         elif num != num[::-1]:
#             result += f"False\n"
#     return result
#
#
# print(is_palindrome(all_numbers)[:-1])