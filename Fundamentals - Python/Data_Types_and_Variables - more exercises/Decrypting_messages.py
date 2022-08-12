key = int(input())
number_of_lines = int(input())
word = ""
for line in range(1, number_of_lines + 1):
    current_letter = input()
    word += chr(key + ord(current_letter))
print(word)
