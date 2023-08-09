from project_functionality.clients.base_client import BaseClient


class Student(BaseClient):
    initial_interest = 2

    def __init__(self,
                 name: str,
                 client_id: str,
                 income: float):
        super().__init__(name,
                         client_id,
                         income,
                         self.initial_interest)
        self.increase_interest = 1

    def increase_clients_interest(self):
        self.interest += self.increase_interest
