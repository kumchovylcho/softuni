beats_per_minute, number_of_beats = int(input()), int(input())
bars = round(number_of_beats / 4, 1)

seconds = int((number_of_beats / beats_per_minute) * 60)
minutes = seconds // 60
seconds_to_print = seconds % 60

if bars.is_integer():
    print(f"{int(bars)} bars - {minutes}m {seconds_to_print}s")
else:
    print(f"{bars:.1f} bars - {minutes}m {seconds_to_print}s")