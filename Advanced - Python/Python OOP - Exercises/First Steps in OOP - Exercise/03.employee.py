class Employee:

    def __init__(self, id: int, first_name, last_name, salary: int):  # NOQA
        self.id = int(id)
        self.first_name = first_name
        self.last_name = last_name
        self.salary = int(salary)

    def get_full_name(self):
        return f"{self.first_name} {self.last_name}"

    def get_annual_salary(self):
        return self.salary * 12

    def raise_salary(self, increase_amount: int):
        self.salary += increase_amount
        return self.salary
