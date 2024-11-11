# advanced_oop.py

# Define a simple class for a bank account
class BankAccount:
    def __init__(self, owner, balance=0):
        # Constructor method to initialize the owner and balance
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        # Method to deposit money into the account
        self.balance += amount
        print(f"{amount} deposited. New balance is: {self.balance}")

    def withdraw(self, amount):
        # Method to withdraw money if sufficient balance
        if amount > self.balance:
            print("Insufficient funds.")
        else:
            self.balance -= amount
            print(f"{amount} withdrawn. New balance is: {self.balance}")

    def get_balance(self):
        # Method to return current balance
        return self.balance

# Create an instance of BankAccount
account = BankAccount("Alice", 100)
account.deposit(50)       # Deposit money
account.withdraw(30)      # Withdraw money
print("Final Balance:", account.get_balance())  # Check balance
