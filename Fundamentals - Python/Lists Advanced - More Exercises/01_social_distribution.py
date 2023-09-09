wealth_numbers = [int(x)for x in input().split(', ')]
minimum_wealth = int(input())

for i in range(len(wealth_numbers)):
    wealthiest = wealth_numbers.index(max(wealth_numbers))

    number = wealth_numbers[i]
    if number < minimum_wealth:
        wealth_difference = minimum_wealth - number
        wealth_numbers[i] += wealth_difference

        wealth_numbers[wealthiest] -= wealth_difference
        if wealth_numbers[wealthiest] < minimum_wealth:
            print('No equal distribution possible')
            break

else:
    print(wealth_numbers)