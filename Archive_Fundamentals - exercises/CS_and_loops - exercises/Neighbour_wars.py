pesho_damage, gosho_damage = int(input()), int(input())
pesho_skill, gosho_skill = 'Roundhouse kick', 'Thunderous fist'
pesho_health, gosho_health = 100, 100

counter = 0

while pesho_health > 0 and gosho_health > 0:
    counter += 1
    if counter % 2 != 0:
        if gosho_health - pesho_damage <= 0:
            gosho_health -= pesho_damage
            break
        else:
            gosho_health -= pesho_damage
            print(f"Pesho used {pesho_skill} and reduced Gosho to {gosho_health} health.")
    elif counter % 2 == 0:
        if pesho_health - gosho_damage <= 0:
            pesho_health -= gosho_damage
            break
        else:
            pesho_health -= gosho_damage
            print(f"Gosho used {gosho_skill} and reduced Pesho to {pesho_health} health.")
    if counter % 3 == 0:
        if gosho_health > 0 and pesho_health > 0:
            gosho_health += 10
            pesho_health += 10
if pesho_health <= 0:
    print(f"Gosho won in {counter}th round.")
elif gosho_health <= 0:
    print(f"Pesho won in {counter}th round.")
