dwarfs = {}
adding_dwarfs = input()
while adding_dwarfs != "Once upon a time":
    name, color, physics = [int(item) if item.isdigit() else item for item in adding_dwarfs.split(" <:> ")]
    dwarfs[color] = dwarfs.get(color, {})
    dwarfs[color][name] = dwarfs[color].get(name, physics)
    if dwarfs[color][name] < physics:
        dwarfs[color][name] = physics
    adding_dwarfs = input()
result = []
for hat in dwarfs:
    for name, physic in dwarfs[hat].items():
        result.append({'length': len(dwarfs[hat]), 'name': name, 'physic': physic, 'hat_color': hat})
for show_result in sorted(result, key=lambda item: (-item['physic'], -item['length'])):
    print(f"({show_result['hat_color']}) {show_result['name']} <-> {show_result['physic']}")
