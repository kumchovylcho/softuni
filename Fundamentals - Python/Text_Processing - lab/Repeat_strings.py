text = input().split()
for word in text:
    print(f"{word * len(word)}", end="")

# text = input().split()
# [print(f"{word * len(word)}", end="") for word in text]
