capacity_of_stadium = int(input())
number_of_all_fans = int(input())
A = 0
B = 0
V = 0
G = 0
for fan in range(1, number_of_all_fans + 1):
    current_sector = input()
    if current_sector == "A":
        A += 1
    elif current_sector == "B":
        B += 1
    elif current_sector == "V":
        V += 1
    elif current_sector == "G":
        G += 1
percentage_A = A / number_of_all_fans * 100
percentage_B = B / number_of_all_fans * 100
percentage_V = V / number_of_all_fans * 100
percentage_G = G / number_of_all_fans * 100
all_fans = (A + B + V + G) / capacity_of_stadium * 100
print(f"{percentage_A:.2f}%\n{percentage_B:.2f}%\n{percentage_V:.2f}%\n{percentage_G:.2f}%\n{all_fans:.2f}%")
