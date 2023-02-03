try:
    with open('text.txt') as file:
        print("File found")

except FileNotFoundError:
    print("File not found")