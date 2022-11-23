import re
ip_pattern = re.compile(r"IP=(?P<ip>.+)\sm")
user_pattern = re.compile(r'user=(?P<user>.+)')
user_logs = {}
command = input()
while command != "end":
    ip = ip_pattern.findall(command)
    ip = ip[0]
    user = user_pattern.findall(command)
    user = user[0]
    user_logs[user] = user_logs.get(user, {})
    user_logs[user][ip] = user_logs[user].get(ip, 0) + 1
    command = input()
for users, ip in sorted(user_logs.items()):
    print(f"{users}:")
    ip_counter = len(ip)
    for counter, address in enumerate(ip, 1):
        if counter < ip_counter:
            print(f"{address} => {user_logs[users][address]}", end=', ')
        elif counter == ip_counter:
            print(f"{address} => {user_logs[users][address]}.")