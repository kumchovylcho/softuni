from project_functionality.loans.base_loan import BaseLoan


class MortgageLoan(BaseLoan):
    INTEREST_RATE = 3.5
    AMOUNT = 50_000.0

    def __init__(self):
        super().__init__(self.INTEREST_RATE,
                         self.AMOUNT)
        self.increase_rate = 0.5

    def increase_interest_rate(self):
        self.interest_rate += self.increase_rate
