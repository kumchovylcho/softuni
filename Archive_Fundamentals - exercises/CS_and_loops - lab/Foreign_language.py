country = input()
languages_spoken = {
    'English': ['England', 'USA'],
    'Spanish': ['Spain', 'Argentina', 'Mexico']
}
for languages in languages_spoken:
    for countries in languages_spoken[languages]:
        if country in countries:
            print(languages)
            break
    if country in countries:
        break
else:
    print("unknown")