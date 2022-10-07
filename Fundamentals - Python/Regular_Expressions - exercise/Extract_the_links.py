import re

pattern = re.compile(r'(?P<sub_domain>w{3}\.)(?P<domain>[A-Za-z0-9\-]+\.)(?P<extension>[a-z]+[\-.]*[a-z0-9\-.]*)')
message = input()
while len(message):
    matches = pattern.finditer(message)
    for match in matches:
        print(f"{match['sub_domain']}{match['domain']}{match['extension']}")
    message = input()