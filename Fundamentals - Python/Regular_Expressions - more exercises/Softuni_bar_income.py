import re
pattern = re.compile(r'(%)(?P<customer>[A-Z][a-z]+)(%)([^\|\$\%\.]*)(<)'
                     r'(?P<product>\w+)(>)([^\|\$\%\.]*)(\|)'
                     r'(?P<count>\d+)(\|)([^\|\$\%\.]*)'
                     r'(?P<price>[1-9]+[.0-9]*)\$')
money_spent_info = []
total_income = 0
command = input()
while command != "end of shift":
    matches = pattern.finditer(command)
    for match in matches:
        name, product = match['customer'], match['product']
        money_spent = int(match['count']) * float(match['price'])
        total_income += money_spent
        money_spent_info.append(f"{name}: {product} - {money_spent:.2f}")
    command = input()
for customers in money_spent_info:
    print(customers)
print(f"Total income: {total_income:.2f}")
