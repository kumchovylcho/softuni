logs = int(input())
logs_aggregator = {}
for _ in range(logs):
    ip, name, duration = [int(x) if x.isdigit() else x for x in input().split()]
    logs_aggregator[name] = logs_aggregator.get(name, {'ip': set(), 'duration': 0})
    logs_aggregator[name]['ip'].add(ip)
    logs_aggregator[name]['duration'] += duration
for name, value in sorted(logs_aggregator.items()):
    total_duration = value['duration']
    all_addresses = ', '.join(sorted(value['ip']))
    print(f"{name}: {total_duration} [{all_addresses}]")
