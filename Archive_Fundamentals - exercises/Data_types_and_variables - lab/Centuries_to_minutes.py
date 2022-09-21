centuries = int(input())
years = centuries * 100
days = int(years * 365.2422)
hours = int(days) * 24
minutes = hours * 60
print(f"{centuries} centuries = {years} years = {days} days = {hours} hours = {minutes} minutes")