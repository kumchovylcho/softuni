from project.wizard import Wizard


class DarkWizard(Wizard):

    def __init__(self, username: str, level: int):
        super().__init__(username, level)

    def __str__(self):
        return f"{self.username} of type {DarkWizard.__name__} has level {self.level}"



# from project.wizard import Wizard
#
#
# class DarkWizard(Wizard):
#
#     def __str__(self):
#         return f"{self.username} of type {DarkWizard.__name__} has level {self.level}"
