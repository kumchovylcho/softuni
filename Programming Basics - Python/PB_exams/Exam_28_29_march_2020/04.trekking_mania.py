from sys import maxsize

peaks = {
    5: 0,
    12: 0,
    25: 0,
    40: 0,
    maxsize: 0
}

number_of_groups = int(input())
for _ in range(number_of_groups):
    number_of_people_in_group = int(input())

    for max_people in peaks:
        if number_of_people_in_group <= max_people:
            peaks[max_people] += number_of_people_in_group
            break


total_people = sum(peaks.values())

for peak, people in peaks.items():
    print(f"{people / total_people * 100:.2f}%")


# number_of_groups = int(input())
# musala = 0
# monblan = 0
# kilimanjaro = 0
# k2 = 0
# everest = 0
# for group in range(1, number_of_groups + 1):
#     number_of_people_in_group = int(input())
#     if number_of_people_in_group <= 5:
#         musala += number_of_people_in_group
#     elif 6 <= number_of_people_in_group <= 12:
#         monblan += number_of_people_in_group
#     elif 13 <= number_of_people_in_group <= 25:
#         kilimanjaro += number_of_people_in_group
#     elif 26 <= number_of_people_in_group <= 40:
#         k2 += number_of_people_in_group
#     else:
#         everest += number_of_people_in_group
# total_people = musala + monblan + kilimanjaro + k2 + everest
# musala_percentage = musala / total_people * 100
# monblan_percentage = monblan / total_people * 100
# kilimanjaro_percentage = kilimanjaro / total_people * 100
# k2_percentage = k2 / total_people * 100
# everest_percentage = everest / total_people * 100
# print(f"{musala_percentage:.2f}%\n{monblan_percentage:.2f}%\n{kilimanjaro_percentage:.2f}%\n{k2_percentage:.2f}%\n{everest_percentage:.2f}%")
