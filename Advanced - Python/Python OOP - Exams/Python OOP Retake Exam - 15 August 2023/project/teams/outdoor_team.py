from project.teams.base_team import BaseTeam


class OutdoorTeam(BaseTeam):

    def __init__(self,
                 name: str,
                 country: str,
                 advantage: int):
        super().__init__(name=name,
                         country=country,
                         advantage=advantage,
                         budget=1_000,
                         )

    def win(self):
        self.advantage += 115
        self.wins += 1
