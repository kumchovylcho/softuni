from project.person import Person


class Child(Person):

    def __init__(self, name: str, age):
        super().__init__(name, age)


# from project.person import Person
#
#
# class Child(Person):
#     pass

