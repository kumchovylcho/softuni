numbers = input().split(", ")


def is_palindrome(number):
    for num in number:
        if num == num[::-1]:
            print("True")
        elif num != num[::-1]:
            print("False")


is_palindrome(numbers)




# numbers = input().split(", ")
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
# print(is_palindrome(numbers)[:-1])