lower_case_words = "dog", "movie", "cat", "coding"
upper_case_words = "DOG", "MOVIE", "CAT", "CODING"
coffees = 0
command = input()
while command != "END":
    if command in lower_case_words:
        coffees += 1
    elif command in upper_case_words:
        coffees += 2
    if command not in lower_case_words + upper_case_words:
        command = input()
        continue
    if coffees > 5:
        break
    command = input()
if command == "END":
    print(coffees)
else:
    print("You need extra sleep")
