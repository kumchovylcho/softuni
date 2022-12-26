from collections import deque


def check_peaks(current_energy):
    for peak, value in peaks_to_conquer.items():
        if value['conq']:
            continue
        if current_energy >= value['diff']:
            peaks_to_conquer[peak]['conq'] = True
        break


peaks_to_conquer = {
    'Vihren': {"diff": 80, "conq": False},
    'Kutelo': {"diff": 90, "conq": False},
    'Banski Suhodol': {"diff": 100, "conq": False},
    'Polezhan': {"diff": 60, "conq": False},
    'Kamenitza': {"diff": 70, "conq": False}
}
food = [int(x) for x in input().split(", ")]
stamina = deque(int(x) for x in input().split(", "))
while food and stamina:
    current_food = food.pop()
    current_stamina = stamina.popleft()
    current_sum = current_food + current_stamina
    check_peaks(current_sum)

if all(True if value['conq'] else False for key, value in peaks_to_conquer.items()):
    print("Alex did it! He climbed all top five Pirin peaks in one week -> @FIVEinAWEEK")
else:
    print("Alex failed! He has to organize his journey better next time -> @PIRINWINS")
if any(True if value['conq'] else False for key, value in peaks_to_conquer.items()):
    print("Conquered peaks:")
    for key, value in peaks_to_conquer.items():
        if value['conq']:
            print(key)


# from collections import deque
#
#
# def check_peaks(current_energy, current_peaks: list):
#     for peak, difficulty in peaks_to_conquer.items():
#         if current_energy >= difficulty:
#             peaks_to_conquer.pop(peak)
#             conquered_peaks.append(peak)
#         break
#     return current_peaks
#
#
# peaks_to_conquer = {
#     'Vihren': 80,
#     'Kutelo': 90,
#     'Banski Suhodol': 100,
#     'Polezhan': 60,
#     'Kamenitza': 70
# }
# conquered_peaks = []
# food = [int(x) for x in input().split(", ")]
# stamina = deque(int(x) for x in input().split(", "))
# while food and stamina:
#     current_food = food.pop()
#     current_stamina = stamina.popleft()
#     current_sum = current_food + current_stamina
#     conquered_peaks = check_peaks(current_sum, conquered_peaks)
# if not peaks_to_conquer:
#     print("Alex did it! He climbed all top five Pirin peaks in one week -> @FIVEinAWEEK")
# if peaks_to_conquer:
#     print("Alex failed! He has to organize his journey better next time -> @PIRINWINS")
# if conquered_peaks:
#     print("Conquered peaks:")
#     print('\n'.join(conquered_peaks))
