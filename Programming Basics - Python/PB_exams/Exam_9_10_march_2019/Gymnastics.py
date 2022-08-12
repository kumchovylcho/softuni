country = input()
sport_device = input()
complexity = 0
performance = 0
if country == "Russia":
    if sport_device == "ribbon":
        complexity = 9.1
        performance = 9.4
    elif sport_device == "hoop":
        complexity = 9.3
        performance = 9.8
    else:
        complexity = 9.6
        performance = 9
elif country == "Bulgaria":
    if sport_device == "ribbon":
        complexity = 9.6
        performance = 9.4
    elif sport_device == "hoop":
        complexity = 9.55
        performance = 9.75
    else:
        complexity = 9.5
        performance = 9.4
else:
    if sport_device == "ribbon":
        complexity = 9.2
        performance = 9.5
    elif sport_device == "hoop":
        complexity = 9.45
        performance = 9.35
    else:
        complexity = 9.7
        performance = 9.15
sum_of_score = complexity + performance
percent_needed_for_max_score = ((20 - sum_of_score) / 20) * 100
print(f"The team of {country} get {sum_of_score:.3f} on {sport_device}.\n{percent_needed_for_max_score:.2f}%")
