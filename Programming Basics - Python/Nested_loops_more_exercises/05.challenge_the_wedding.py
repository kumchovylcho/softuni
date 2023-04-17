number_of_men = int(input())
number_of_women = int(input())
tables = int(input())
current_tables = 0
for men in range(1, number_of_men + 1):
    for women in range(1, number_of_women + 1):
        if current_tables == tables:
            break
        else:
            print(f"({men} <-> {women})", end=" ")
            current_tables += 1
