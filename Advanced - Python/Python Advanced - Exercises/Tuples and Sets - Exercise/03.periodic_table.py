chemical_elements = int(input())
unique_elements = set()
for _ in range(chemical_elements):
    current_element = input().split()
    [unique_elements.add(element) for element in current_element]
[print(element) for element in unique_elements]