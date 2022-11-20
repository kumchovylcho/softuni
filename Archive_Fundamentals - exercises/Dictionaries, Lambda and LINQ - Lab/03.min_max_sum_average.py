results = {
    'all_numbers': [],
    'sum': 0,
    'min': 1000000,
    'max': -1000000,
    'average': 0
}
numbers = int(input())
for _ in range(numbers):
    current_number = int(input())
    results['all_numbers'].append(current_number)
results['sum'] = sum(results['all_numbers'])
results['min'] = min(results['all_numbers'])
results['max'] = max(results['all_numbers'])
results['average'] = sum(results['all_numbers']) / len(results['all_numbers'])
print(f"Sum = {results['sum']}")
print(f"Min = {results['min']}")
print(f"Max = {results['max']}")
print(f"Average = {results['average']}")