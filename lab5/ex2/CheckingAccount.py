from Account import Account


class CheckingAccount(Account):
    def __init__(self, account_number, balance, overdraft_limit=100):
        super().__init__(account_number, balance)
        self.overdraft_limit = overdraft_limit

    def withdraw(self, amount):
        if amount < 0:
            print("Invalid number to withdraw.")
        elif amount > (self.balance + self.overdraft_limit):
            print("Transaction declined. Exceeds overdraft limit.")
        else:
            self.balance -= amount
            print(f"Withdrew ${amount}. New balance: ${self.balance}")
