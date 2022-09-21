photo_number = int(input())
day, month, year = int(input()), int(input()), int(input())
hours, minutes = int(input()), int(input())
size = int(input())
width, height = int(input()), int(input())

volume = ''
if size < 1000:
    volume = 'B'
elif size <= 10000:
    size /= 10
    volume = 'KB'
elif size <= 100000:
    size /= 100
    volume = 'KB'
elif size < 1000000:
    size /= 1000
    volume = 'KB'
elif size >= 1000000:
    size /= 1000000
    volume = 'MB'

portrait = ''
if width > height:
    portrait = '(landscape)'
elif height > width:
    portrait = '(portrait)'
elif width == height:
    portrait = '(square)'

print(f"Name: DSC_{photo_number:04d}.jpg")
print(f"Date Taken: {day:02d}/{month:02d}/{year} {hours:02d}:{minutes:02d}")
size = str(size)
if "." in size:
    index_of_dot = size.index(".")
    if size[index_of_dot + 1] == "0":
        print(f"Size: {float(size):.0f}{volume}")
    else:
        size = float(size)
        print(f"Size: {size:.1f}{volume}")
elif "." not in size:
    size = int(size)
    print(f"Size: {size}{volume}")
print(f"Resolution: {width}x{height} {portrait}")

