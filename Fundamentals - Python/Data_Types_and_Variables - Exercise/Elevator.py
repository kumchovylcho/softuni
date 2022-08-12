from math import ceil
number_of_persons = int(input())
capacity_of_persons = int(input())
courses = ceil(number_of_persons / capacity_of_persons)
print(courses)
