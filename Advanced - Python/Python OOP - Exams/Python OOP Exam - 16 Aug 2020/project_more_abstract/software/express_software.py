from project.software.software import Software


class ExpressSoftware(Software):

    def __init__(self, name: str, capacity_consumption: int, memory_consumption: int):
        super().__init__(name,
                         self.__software_type,
                         capacity_consumption,
                         memory_consumption * 2,
                         )

    @property
    def __software_type(self):
        return "Express"