budget = float(input())
number_video_cards = int(input())
number_cpus = int(input())
number_rams = int(input())
video_card = 250 * number_video_cards
cpu = (video_card * 0.35) * number_cpus
ram = (video_card * 0.10) * number_rams
total_price = video_card + cpu + ram
if number_video_cards > number_cpus:
    total_price *= 0.85
if total_price <= budget:
    diff = total_price - budget
    print(f"You have {abs(diff):.2f} leva left!")
else:
    diff = total_price - budget
    print(f"Not enough money! You need {diff:.2f} leva more!")
