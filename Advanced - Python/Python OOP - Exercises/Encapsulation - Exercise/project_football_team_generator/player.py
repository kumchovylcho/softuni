class Player:

    def __init__(self, name: str, sprint: int, dribble: int, passing: int, shooting: int):
        self.__name = name
        self.__sprint = sprint
        self.__dribble = dribble
        self.__passing = passing
        self.__shooting = shooting

    @property
    def name(self):
        return self.__name

    def __str__(self):
        output = [f"Player: {self.name}", f"Sprint: {self.__sprint}", f"Dribble: {self.__dribble}",
                  f"Passing: {self.__passing}", f"Shooting: {self.__shooting}"]
        return '\n'.join(output)


# class Player:
#
#     def __init__(self, name: str, sprint: int, dribble: int, passing: int, shooting: int):
#         self.__name = name
#         self.__sprint = int(sprint)
#         self.__dribble = int(dribble)
#         self.__passing = int(passing)
#         self.__shooting = int(shooting)
#
#     @property
#     def __name(self):
#         return self.name
#
#     @__name.setter
#     def __name(self, value):
#         self.name = value
#
#     def __str__(self):
#         return f"Player: {self.__name}\n" \
#                f"Sprint: {self.__sprint}\n" \
#                f"Dribble: {self.__dribble}\n" \
#                f"Passing: {self.__passing}\n" \
#                f"Shooting: {self.__shooting}\n"
