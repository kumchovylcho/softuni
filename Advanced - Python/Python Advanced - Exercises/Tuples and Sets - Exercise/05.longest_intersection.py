lines = int(input())   # not my solution
max_intersection = 0
combined_intersection = set()
set_a = set()
set_b = set()

for i in range(lines):
    data = input().split("-")
    range_1 = [int(i) for i in data[0].split(",")]
    range_2 = [int(i) for i in data[1].split(",")]
    for i in range(range_1[0], range_1[1] + 1):
        set_a.add(i)
    for i in range(range_2[0], range_2[1] + 1):
        set_b.add(i)
    sets_intersection = set_a.intersection(set_b)
    if len(sets_intersection) > max_intersection:
        max_intersection = len(sets_intersection)
        combined_intersection = sets_intersection
    set_a.clear()
    set_b.clear()


print(f"Longest intersection is [", end="")
print(*combined_intersection, sep=", ", end="")
print(f"] with length {max_intersection}")