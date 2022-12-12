bands = {}
command = input()
while command != "Start!":
    command = command.split("; ")
    task = command[0]
    band_name = command[1]
    if task == "Add":
        members = command[2].split(", ")
        if band_name not in bands:
            bands[band_name] = {'members': [], 'time': 0}
        for name in members:
            if name not in bands[band_name]['members']:
                bands[band_name]['members'].append(name)
    elif task == "Play":
        time = int(command[2])
        if band_name not in bands:
            bands[band_name] = {'members': [], 'time': 0}
        bands[band_name]['time'] += time
    command = input()
total_time = 0
all_bands, first_band = [], []
for band, value in bands.items():
    if not total_time:
        first_band.append(band)
        for name in value['members']:
            first_band.append(f"=> {name}")
    total_time += value['time']
    all_bands.append(f"{band} -> {value['time']}")
print(f"Total time: {total_time}")
print('\n'.join(all_bands))
print('\n'.join(first_band))
