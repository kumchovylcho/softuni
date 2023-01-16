class Username:

    def __init__(self):
        self.unique_names = set()

    def add_user(self, name):
        self.unique_names.add(name)

    def __repr__(self):
        return '\n'.join(self.unique_names)


unique_usernames = Username()
number_of_names = int(input())
for _ in range(number_of_names):
    current_name = input()
    unique_usernames.add_user(current_name)


print(unique_usernames)


# number_of_names = int(input())
# unique_names = set()
# for _ in range(number_of_names):
#     name = input()
#     unique_names.add(name)
# print('\n'.join(unique_names))