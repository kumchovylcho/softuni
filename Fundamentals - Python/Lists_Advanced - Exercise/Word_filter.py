# words = input().split()
#
#
# def even_length(text):
#     for word in text:
#         if len(word) % 2 == 0:
#             print(word)
#
#
# even_length(words)

words = input().split()
filtered = [print(word) for word in words if len(word) % 2 == 0]
