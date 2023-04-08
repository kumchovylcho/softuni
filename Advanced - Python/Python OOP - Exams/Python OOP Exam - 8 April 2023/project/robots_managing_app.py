from project_oop.robots.female_robot import FemaleRobot
from project_oop.robots.male_robot import MaleRobot
from project_oop.services.main_service import MainService
from project_oop.services.secondary_service import SecondaryService


class RobotsManagingApp:

    def __init__(self):
        self.robots = []
        self.services = []

    @property
    def service_types(self):
        return {
                "MainService": MainService,
                "SecondaryService": SecondaryService,
                }

    @property
    def robot_types(self):
        return {
                "MaleRobot": MaleRobot,
                "FemaleRobot": FemaleRobot,
                }

    @staticmethod
    def find_object(item: str, attribute: str, collection: list):
        for obj in collection:
            if getattr(obj, attribute) == item:
                return obj

    def add_service(self, service_type: str, name: str):
        if service_type not in self.service_types:
            raise Exception("Invalid service type!")

        self.services.append(self.service_types[service_type](name))

        return f"{service_type} is successfully added."


    def add_robot(self, robot_type: str, name: str, kind: str, price: float):
        if robot_type not in self.robot_types:
            raise Exception("Invalid robot type!")

        self.robots.append(self.robot_types[robot_type](name, kind, price))

        return f"{robot_type} is successfully added."


    def add_robot_to_service(self, robot_name: str, service_name: str):
        robot = self.find_object(robot_name, "name", self.robots)
        service = self.find_object(service_name, "name", self.services)

        invalid_robot_services = {
            "FemaleRobot": "MainService",
            "MaleRobot": "SecondaryService",
        }

        for rob_name, serv_name in invalid_robot_services.items():
            if type(robot).__name__ == rob_name and type(service).__name__ == serv_name:
                return "Unsuitable service."

        if len(service.robots) + 1 > service.capacity:
            raise Exception("Not enough capacity for this robot!")

        self.robots.remove(robot)
        service.robots.append(robot)

        return f"Successfully added {robot_name} to {service_name}."

    def remove_robot_from_service(self, robot_name: str, service_name: str):
        service = self.find_object(service_name, "name", self.services)
        robot = self.find_object(robot_name, "name", service.robots)

        if not robot:
            raise Exception("No such robot in this service!")

        service.robots.remove(robot)
        self.robots.append(robot)

        return f"Successfully removed {robot_name} from {service_name}."

    def feed_all_robots_from_service(self, service_name: str):
        service = self.find_object(service_name, "name", self.services)

        fed_robots = 0
        for robot in service.robots:
            robot.eating()
            fed_robots += 1

        return f"Robots fed: {fed_robots}."

    def service_price(self, service_name: str):
        service = self.find_object(service_name, "name", self.services)

        all_robots_price = sum(robot.price for robot in service.robots)

        return f"The value of service {service_name} is {all_robots_price:.2f}."

    def __str__(self):
        output = []

        for service in self.services:
            output.append(service.details())

        return '\n'.join(output)
