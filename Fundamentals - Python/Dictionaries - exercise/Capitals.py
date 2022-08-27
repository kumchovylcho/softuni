countries = input().split(", ")
capitals = input().split(", ")
country_information = {key: value for key, value in zip(countries, capitals)}

[print(f"{country} -> {country_information[country]}")for country in country_information]


# countries = input().split(", ")
# capitals = input().split(", ")
#
# pairs = dict()
#
# capital_counter = 0
# for country in countries:
#     pairs[country] = capitals[capital_counter]
#     capital_counter += 1
#
# [print(f"{pair} -> {pairs[pair]}") for pair in pairs]