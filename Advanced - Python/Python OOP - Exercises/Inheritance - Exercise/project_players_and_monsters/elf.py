from project.hero import Hero


class Elf(Hero):

    def __init__(self, username: str, level: int):
        super().__init__(username, level)

    def __str__(self):
        return f"{self.username} of type {Elf.__name__} has level {self.level}"


# from project.hero import Hero
#
#
# class Elf(Hero):
#
#     def __str__(self):
#         return f"{self.username} of type {Elf.__name__} has level {self.level}"
