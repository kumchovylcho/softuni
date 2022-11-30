def palindrome(word, index):
    if word == word[::-1]:
        return f"{word} is a palindrome"
    return f"{word} is not a palindrome"
