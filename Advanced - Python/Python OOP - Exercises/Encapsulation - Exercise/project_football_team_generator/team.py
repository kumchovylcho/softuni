from project.player import Player


class Team:

    def __init__(self, name: str, rating: int):
        self.__name = name
        self.__rating = int(rating)
        self.__players = []

    def add_player(self, player: Player):
        for info in self.__players:
            if player.name == info.name:
                return f"Player {player.name} has already joined"
        self.__players.append(player)
        return f"Player {player.name} joined team {self.__name}"

    def remove_player(self, player_name: str):
        for info in self.__players:
            if info.name == player_name:
                self.__players.remove(info)
                return info
        return f"Player {player_name} not found"
