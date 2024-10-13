class BankAccount:
    def __init__(self, balance=0):
        self._balance = balance  # Convention: _variable means it's a protected variable

    def deposit(self, amount):
        self._balance += amount

    def withdraw(self, amount):
        if amount <= self._balance:
            self._balance -= amount
        else:
            print("Insufficient funds")

    def get_balance(self):
        return self._balance


# Creating an instance of the BankAccount class
account = BankAccount()

# Performing transactions
account.deposit(1000)
account.withdraw(500)
print(f"Current balance: {account.get_balance()}")




