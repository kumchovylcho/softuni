username = input()
password = input()
current_password = input()
while current_password != password:
    current_password = input()
print(f"Welcome {username}!")
