from project.hardware.hardware import Hardware


class PowerHardware(Hardware):

    def __init__(self, name: str, capacity: int, memory: int):
        super().__init__(name,
                         self.__hardware_type,
                         int(capacity * 0.25),
                         int(memory * 1.75)
                         )

    @property
    def __hardware_type(self):
        return "Power"