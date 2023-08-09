from project_functionality.clients.adult import Adult
from project_functionality.clients.student import Student
from project_functionality.loans.mortgage_loan import MortgageLoan
from project_functionality.loans.student_loan import StudentLoan


class BankApp:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.loans = []
        self.clients = []

    @property
    def valid_loans(self):
        return {"StudentLoan": StudentLoan,
                "MortgageLoan": MortgageLoan}

    @property
    def valid_clients(self):
        return {"Student": Student,
                "Adult": Adult}

    @staticmethod
    def get_object(item: str, attribute: str, collection: list):
        for obj in collection:
            if getattr(obj, attribute) == item:
                return obj

        return None

    @staticmethod
    def get_loan(loan_type: str, collection: list):
        for obj in collection:
            if type(obj).__name__ == loan_type:
                return obj

        return None

    def add_loan(self, loan_type: str):
        if loan_type not in self.valid_loans:
            raise Exception("Invalid loan type!")

        self.loans.append(self.valid_loans[loan_type]())

        return f"{loan_type} was successfully added."

    def add_client(self,
                   client_type: str,
                   client_name: str,
                   client_id: str,
                   income: float):
        if client_type not in self.valid_clients:
            raise Exception("Invalid client type!")

        if len(self.clients) == self.capacity:
            return "Not enough bank capacity."

        self.clients.append(self.valid_clients[client_type](name=client_name,
                                                            client_id=client_id,
                                                            income=income))

        return f"{client_type} was successfully added."


    def grant_loan(self, loan_type: str, client_id: str):
        client = self.get_object(client_id, "client_id", self.clients)
        loan = self.get_loan(loan_type, self.loans)

        invalid_client_loans = {
            "Student": "MortgageLoan",
            "Adult": "StudentLoan"
        }

        if invalid_client_loans[type(client).__name__] == loan_type:
            raise Exception("Inappropriate loan type!")

        self.loans.remove(loan)
        client.loans.append(loan)

        return f"Successfully granted {loan_type} to {client.name} with ID {client_id}."

    def remove_client(self, client_id: str):
        client = self.get_object(client_id, "client_id", self.clients)

        if not client:
            raise Exception("No such client!")

        if client.loans:
            raise Exception("The client has loans! Removal is impossible!")

        self.clients.remove(client)

        return f"Successfully removed {client.name} with ID {client_id}."

    def increase_loan_interest(self, loan_type: str):
        loans_changed = 0
        for loan in self.loans:
            if type(loan).__name__ == loan_type:
                loan.increase_interest_rate()
                loans_changed += 1

        return f"Successfully changed {loans_changed} loans."

    def increase_clients_interest(self, min_rate: float):
        changed_clients = 0
        for client in self.clients:
            if client.interest < min_rate:
                client.increase_clients_interest()
                changed_clients += 1

        return f"Number of clients affected: {changed_clients}."

    def get_statistics(self):
        total_income = 0
        granted_loans = 0
        granted_sum = 0
        not_granted_sum = sum(loan.amount for loan in self.loans)
        all_interest_rates = 0

        for client in self.clients:
            total_income += client.income
            granted_loans += len(client.loans)
            all_interest_rates += client.interest

            for loan in client.loans:
                granted_sum += loan.amount

        average_client_interest_rate = 0 if not self.clients else all_interest_rates / len(self.clients)

        result = [
            f"Active Clients: {len(self.clients)}",
            f"Total Income: {total_income:.2f}",
            f"Granted Loans: {granted_loans}, Total Sum: {granted_sum:.2f}",
            f"Available Loans: {len(self.loans)}, Total Sum: {not_granted_sum:.2f}",
            f"Average Client Interest Rate: {average_client_interest_rate:.2f}"
        ]

        return "\n".join(result)



