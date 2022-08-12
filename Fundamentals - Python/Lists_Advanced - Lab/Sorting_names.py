names_list = input().split(", ")
sorted_list = sorted(names_list, key=lambda x: (-len(x), x))
print(sorted_list)