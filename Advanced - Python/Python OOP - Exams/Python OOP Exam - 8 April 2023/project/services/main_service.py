from project_oop.services.base_service import BaseService


class MainService(BaseService):

    def __init__(self, name: str):
        super().__init__(name, self.initial_capacity)

    @property
    def initial_capacity(self):
        return 30

    def details(self):
        output = [f"{self.name} Main Service:"]

        if self.robots:
            output.append(f"Robots: {', '.join(robot.name for robot in self.robots)}")

        elif not self.robots:
            output.append(f"Robots: none")

        return '\n'.join(output)