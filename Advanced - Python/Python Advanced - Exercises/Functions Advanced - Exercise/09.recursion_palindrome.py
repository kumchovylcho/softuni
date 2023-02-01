def palindrome(word, index, right_index=-1):
    if index == len(word) // 2:
        return f"{word} is a palindrome"

    if word[index] != word[right_index]:
        return f"{word} is not a palindrome"

    return palindrome(word, index + 1, right_index - 1)


# def palindrome(word, index):
#     if word == word[::-1]:
#         return f"{word} is a palindrome"
#     return f"{word} is not a palindrome"
