pokemons = [int(n) for n in input().split()]
sum_of_captures_pokemons = []


def capture_pokemons(index, pokemons):
    first_element = int(pokemons[0])
    last_element = int(pokemons[-1])
    if index < 0:
        sum_of_captures_pokemons.append(first_element)  # appends the first element
        del pokemons[0]                     # deletes element at current_index 0
        pokemons.insert(0, last_element)    # puts last element to current_index 0

    elif index > len(pokemons) - 1:
        sum_of_captures_pokemons.append(last_element)  # appends the last element
        del pokemons[-1]                    # deletes element at current_index -1
        pokemons.insert(len(pokemons), first_element)  # puts first element at current_index -1

    if 0 <= index < len(pokemons):
        if index == len(pokemons):
            sum_of_captures_pokemons.append(pokemons[index - 1])
            del pokemons[index - 1]
        else:
            sum_of_captures_pokemons.append(pokemons[index])
            del pokemons[index]

    for counter, number in enumerate(pokemons):
        if number <= sum_of_captures_pokemons[-1]:
            pokemons[counter] = number + sum_of_captures_pokemons[-1]
        elif number > sum_of_captures_pokemons[-1]:
            pokemons[counter] = number - sum_of_captures_pokemons[-1]


while len(pokemons) > 0:
    current_position = int(input())
    capture_pokemons(current_position, pokemons)

print(sum(sum_of_captures_pokemons))
