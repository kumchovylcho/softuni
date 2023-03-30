a = int(input())
b = int(input())
max_passwords = int(input())

symbol_positions = {
    'a': {'current': 35, 'start': 35, 'end': 55},
    'b': {'current': 64, 'start': 64, 'end': 96},
}

generated_passwords = 0

limit_reached = False

for one in range(1, a + 1):
    for two in range(1, b + 1):
        first_symbol, second_symbol = chr(symbol_positions['a']['current']), chr(symbol_positions['b']['current'])
        print(f"{first_symbol}{second_symbol}{one}{two}{second_symbol}{first_symbol}", end="|")

        generated_passwords += 1

        for x in symbol_positions.values():
            x['current'] += 1

            if x['current'] > x['end']:
                x['current'] = x['start']

        if generated_passwords == max_passwords:
            limit_reached = True

        if limit_reached:
            break
    if limit_reached:
        break
