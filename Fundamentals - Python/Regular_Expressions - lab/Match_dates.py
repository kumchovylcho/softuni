import re
dates = input()
pattern = re.compile(r'\b(?P<day>\d{2})([\\.\-/])(?P<month>[A-Z][a-z]{2})\2(?P<year>\d{4})\b')
matches = re.finditer(pattern, dates)
for date in matches:
    print(f"Day: {date['day']}, Month: {date['month']}, Year: {date['year']}")
