first_guy = int(input())
second_guy = int(input())
third_guy = int(input())
total_seconds = first_guy + second_guy + third_guy
minutes = total_seconds // 60
seconds = total_seconds % 60
if seconds < 10:
    print(f"{minutes}:0{seconds}")
else:
    print(f"{minutes}:{seconds}")
