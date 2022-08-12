searched_book = input()
books_searched = 0
is_found = False
current_book = input()
while current_book != "No More Books":
    if current_book == searched_book:
        is_found = True
        break
    books_searched += 1
    current_book = input()
if current_book == "No More Books":
    print(f"The book you search is not here!\nYou checked {books_searched} books.")
if is_found:
    print(f"You checked {books_searched} books and found it.")
