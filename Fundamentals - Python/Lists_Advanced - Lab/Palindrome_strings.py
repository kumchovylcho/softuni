words = input().split()
palindrome = input()
palindrome_words = []


def is_palindrome(string):
    for word in string:
        if word == palindrome[::-1]:
            palindrome_words.append(word)
        elif word == word[::-1]:
            palindrome_words.append(word)
    return palindrome_words


print(is_palindrome(words))
print(f"Found palindrome {palindrome_words.count(palindrome)} times")