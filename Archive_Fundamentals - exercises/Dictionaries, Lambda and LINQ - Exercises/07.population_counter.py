population = {}
country_info = input()
while country_info != "report":
    city, country, people = [int(x) if x.isdigit() else x for x in country_info.split("|")]
    population[country] = population.get(country, {'city': [], 'people': []})
    population[country]['city'].append(city)
    population[country]['people'].append(people)
    country_info = input()
for countries, cities in sorted(population.items(), key=lambda x: -sum(x[1]['people'])):
    print(f"{countries} (total population: {sum(cities['people'])})")
    for city_ in sorted(zip(cities['city'], cities['people']), key=lambda x: -x[1]):
        print(f"=>{city_[0]}: {city_[1]}")
