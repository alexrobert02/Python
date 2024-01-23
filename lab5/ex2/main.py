from SavingsAccount import SavingsAccount
from CheckingAccount import CheckingAccount


def main():
    print("Savings Account:")
    savings_account = SavingsAccount("SA001", 1000)
    savings_account.deposit(500)
    savings_account.withdraw(200)
    savings_account.calculate_interest()

    print("\nChecking Account:")
    checking_account = CheckingAccount("CA001", 500, 200)
    checking_account.withdraw(700)
    checking_account.deposit(100)
    checking_account.withdraw(150)


if __name__ == '__main__':
    main()
