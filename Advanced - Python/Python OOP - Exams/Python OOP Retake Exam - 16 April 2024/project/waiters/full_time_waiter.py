from project.waiters.base_waiter import BaseWaiter


class FullTimeWaiter(BaseWaiter):

    def __init__(self, name: str, hours_worked: int):
        super().__init__(name, hours_worked)
        self.hourly_wage = 15

    def calculate_earnings(self):
        return self.hours_worked * self.hourly_wage

    def report_shift(self):
        return f"{self.name} worked a full-time shift of {self.hours_worked} hours."

