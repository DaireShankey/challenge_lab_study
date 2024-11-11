# custom_exceptions.py

# Define a custom exception for insufficient funds
class InsufficientFundsError(Exception):
    def __init__(self, message="Insufficient funds for this operation."):
        self.message = message
        super().__init__(self.message)

# Function to demonstrate custom exception
def withdraw_funds(balance, amount):
    if amount > balance:
        raise InsufficientFundsError(f"Attempted to withdraw {amount} with balance of {balance}")
    else:
        return balance - amount

# Try to withdraw more than the balance
try:
    balance = 100
    new_balance = withdraw_funds(balance, 150)
    print("New balance:", new_balance)
except InsufficientFundsError as e:
    print("Error:", e)
