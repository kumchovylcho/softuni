numbers = int(input())
p1 = 0
p2 = 0
p3 = 0
p4 = 0
p5 = 0
for number in range(1, numbers + 1):
    current_number = int(input())
    if current_number < 200:
        p1 += 1
    elif 200 <= current_number <= 399:
        p2 += 1
    elif 400 <= current_number <= 599:
        p3 += 1
    elif 600 <= current_number <= 799:
        p4 += 1
    else:
        p5 += 1
p1_perc = (p1 / numbers) * 100
p2_perc = (p2 / numbers) * 100
p3_perc = (p3 / numbers) * 100
p4_perc = (p4 / numbers) * 100
p5_perc = (p5 / numbers) * 100
print(f"{p1_perc:.2f}%\n{p2_perc:.2f}%\n{p3_perc:.2f}%\n{p4_perc:.2f}%\n{p5_perc:.2f}%")
