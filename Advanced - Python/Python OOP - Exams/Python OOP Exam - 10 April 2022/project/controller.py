


class Controller:

    def __init__(self):
        self.players = []
        self.supplies = []

    def __find_player(self, name: str):
        for player in self.players:
            if player.name == name:
                return player

    def add_player(self, *players):
        added = []
        for x in players:
            if x not in self.players:
                self.players.append(x)
                added.append(x)
        return f"Successfully added: {', '.join(x.name for x in added)}"

    def add_supply(self, *supplies):
        for x in supplies:
            self.supplies.append(x)

    def sustain(self, player_name: str, sustenance_type: str):
        player = self.__find_player(player_name)

        if not player or sustenance_type not in ("Food", "Drink"):
            return

        if sustenance_type == "Food" and not [x for x in self.supplies if type(x).__name__ == "Food"]:
            raise Exception("There are no food supplies left!")

        if sustenance_type == "Drink" and not [x for x in self.supplies if type(x).__name__ == "Drink"]:
            raise Exception("There are no drink supplies left!")

        if not player.need_sustenance:
            return f"{player_name} have enough stamina."

        if sustenance_type == "Food":
            pos, food = [(index, x) for index, x in enumerate(self.supplies) if type(x).__name__ == "Food"][-1]
            if player.stamina + food.energy > 100:
                player.stamina = 100
            else:
                player.stamina += food.energy
            self.supplies.pop(pos)
            return f"{player_name} sustained successfully with {food.name}."

        elif sustenance_type == "Drink":
            pos, drink = [(index, x) for index, x in enumerate(self.supplies) if type(x).__name__ == "Drink"][-1]

            if player.stamina + drink.energy > 100:
                player.stamina = 100
            else:
                player.stamina += drink.energy
            self.supplies.pop(pos)
            return f"{player_name} sustained successfully with {drink.name}."

    def duel(self, first_player_name: str, second_player_name: str):
        first_player = self.__find_player(first_player_name)
        second_player = self.__find_player(second_player_name)

        if not first_player.stamina and not second_player.stamina:
            return f"Player {first_player.name} does not have enough stamina.\n" \
                   f"Player {second_player.name} does not have enough stamina."

        if not first_player.stamina:
            return f"Player {first_player.name} does not have enough stamina."

        if not second_player.stamina:
            return f"Player {second_player.name} does not have enough stamina."

        sort_players_by_stamina = [x for x in sorted([first_player, second_player], key=lambda x: x.stamina)]

        first_player_attack, second_player_attack = sort_players_by_stamina[0], sort_players_by_stamina[1]

        if second_player_attack.stamina - (first_player_attack.stamina / 2) <= 0:
            second_player_attack.stamina = 0
            return f"Winner: {first_player_attack.name}"
        else:
            second_player_attack.stamina -= first_player_attack.stamina / 2

        if first_player_attack.stamina - (second_player_attack.stamina / 2) <= 0:
            first_player_attack.stamina = 0
            return f"Winner: {second_player_attack.name}"
        else:
            first_player_attack.stamina -= second_player_attack.stamina / 2

        player_with_more_stamina = [x for x in sorted(sort_players_by_stamina, key=lambda x: -x.stamina)][0]
        return f"Winner: {player_with_more_stamina.name}"

    def next_day(self):
        for player in self.players:
            if player.stamina - (player.age * 2) < 0:
                player.stamina = 0
            else:
                player.stamina -= player.age * 2

        for player in self.players:
            for food in ("Food", "Drink"):
                self.sustain(player.name, food)

    def __str__(self):
        output = []
        for player in self.players:
            output.append(str(player))

        for supply in self.supplies:
            output.append(supply.details())

        return '\n'.join(output)
