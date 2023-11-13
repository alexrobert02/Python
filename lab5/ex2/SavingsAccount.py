from Account import Account


class SavingsAccount(Account):
    def __init__(self, account_number, balance, interest_rate=0.02):
        super().__init__(account_number, balance)
        self.interest_rate = interest_rate

    def calculate_interest(self):
        interest = self.balance * self.interest_rate
        self.deposit(interest)
        print("Interest calculated:", interest)
