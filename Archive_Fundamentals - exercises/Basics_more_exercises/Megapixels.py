width, height = int(input()), int(input())
result = round(((width * height) / 1000000), 1)
if result.is_integer():
    print(f"{width}x{height} => {int(result)}MP")
else:
    print(f"{width}x{height} => {result}MP")
