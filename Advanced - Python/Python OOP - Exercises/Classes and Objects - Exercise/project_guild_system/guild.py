from project.player import Player


class Guild:

    def __init__(self, name: str):
        self.name = name
        self.players = []

    def assign_player(self, player: Player):
        if player.guild == self.name:
            return f"Player {player.name} is already in the guild."

        if player.guild != "Unaffiliated":
            return f"Player {player.name} is in another guild."

        self.players.append(player)
        player.guild = self.name

        return f"Welcome player {player.name} to the guild {self.name}"

    def kick_player(self, player_name: str):
        for player in self.players:
            if player.name == player_name:
                player.guild = "Unaffiliated"
                self.players.remove(player)

                return f"Player {player_name} has been removed from the guild."

        return f"Player {player_name} is not in the guild."

    def guild_info(self):
        result = [f"Guild: {self.name}"]

        [result.append(player.player_info()) for player in self.players]

        return '\n'.join(result)


player = Player("George", 50, 100)
print(player.add_skill("Shield Break", 20))
print(player.player_info())
guild = Guild("UGT")
print(guild.assign_player(player))
print(guild.guild_info())


# from project.player import Player
#
#
# class Guild:
#
#     def __init__(self, name: str):
#         self.name = name
#         self.players = []
#
#     def assign_player(self, player: Player):
#         if player in self.players:
#             return f"Player {player.name} is already in the guild."
#         if player.guild != "Unaffiliated" and player.guild != self.name:
#             return f"Player {player.name} is in another guild."
#         self.players.append(player)
#         player.guild = self.name
#         return f"Welcome player {player.name} to the guild {self.name}"
#
#     def kick_player(self, player_name: str):
#         for name in self.players:
#             if name.name == player_name:
#                 name.guild = "Unaffiliated"
#                 self.players.remove(name)
#                 return f"Player {player_name} has been removed from the guild."
#         return f"Player {player_name} is not in the guild."
#
#     def guild_info(self):
#         output = [f"Guild: {self.name}"]
#         for member in self.players:
#             output.append(member.player_info())
#         return '\n'.join(output)


# from project.player import Player
#
#
# class Guild:
#
#     def __init__(self, name: str):
#         self.name = name
#         self.players = []
#
#     def assign_player(self, player: Player):
#         if player.guild == self.name:
#             return f"Player {player.name} is already in the guild."
#         elif player.guild == "Unaffiliated":
#             player.guild = self.name
#             self.players.append(player)
#             return f"Welcome player {player.name} to the guild {self.name}"
#         return f"Player {player.name} is in another guild."
#
#     def kick_player(self, player_name: str):
#         for player in self.players:
#             if player.name == player_name:
#                 player.guild = "Unaffiliated"
#                 self.players.remove(player)
#                 return f"Player {player_name} has been removed from the guild."
#         return f"Player {player_name} is not in the guild."
#
#     def guild_info(self):
#         output = f"Guild: {self.name}\n"
#         for players in self.players:
#             output += f"{players.player_info()}\n"
#         return output
