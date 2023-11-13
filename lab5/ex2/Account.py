class Account:
    def __init__(self, account_number, balance):
        self.account_number = account_number
        self.balance = balance
        print(f"Initial balance: ${self.balance}")

    def deposit(self, amount):
        if amount < 0:
            print("Invalid number to deposit.")
        else:
            self.balance += amount
            print(f"Deposited ${amount}. New balance: ${self.balance}")

    def withdraw(self, amount):
        if amount < 0:
            print("Invalid number to withdraw.")
        elif amount > self.balance:
            print("Insufficient funds!")
        else:
            self.balance -= amount
            print(f"Withdrew ${amount}. New balance: ${self.balance}")

    def calculate_interest(self):
        pass
