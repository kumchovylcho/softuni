profession = input()

drink_chooser = {
    'Athlete': 'Water',
    'Businessman': 'Coffee',
    'Businesswoman': 'Coffee',
    'SoftUni Student': 'Beer',
}

print(drink_chooser.get(profession, "Tea"))
