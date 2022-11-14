clothes = [int(number) for number in input().split()]
rack_capacity = int(input())
racks = []
racks_counter = 0
for cloth in range(len(clothes) - 1, -1, -1):
    current_cloth = clothes.pop()
    racks.append(current_cloth)
    if sum(racks) == rack_capacity:
        if clothes:
            racks = []
            racks_counter += 1
    elif sum(racks) > rack_capacity:
        racks = [current_cloth]
        racks_counter += 1
if racks:
    racks_counter += 1

print(racks_counter)
