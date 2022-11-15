unique_names = set()
number_of_names = int(input())
for name in range(number_of_names):
    current_name = input()
    unique_names.add(current_name)
print('\n'.join(unique_names))