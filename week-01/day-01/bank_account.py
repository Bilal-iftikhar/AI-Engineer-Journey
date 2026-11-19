
from datetime import datetime


class InsufficientFundsError(Exception):
    pass


class BankAccount:

    def __init__(self, owner: str, balance: float = 0.0):
        if balance < 0:
            raise ValueError("Initial balance cannot be negative")
        self.owner = owner
        self._balance = balance
        self.transactions: list[str] = []

    @property
    def balance(self) -> float:
        return self._balance

    def deposit(self, amount: float) -> None:
        if(amount <= 0):
            raise ValueError("Amount must be greater than zero")
        
        self._balance += amount
        self.transactions.append(f"{datetime.now()} - Deposited: {amount}")
        return

    def withdraw(self, amount: float) -> None:
        if(amount <= 0):
            raise ValueError("Amount must be greater than zero")
        
        if(amount > self._balance):
            raise InsufficientFundsError("Insufficient account balance")
        
        self._balance -= amount
        self.transactions.append(f"{datetime.now()} - Withdrawl: {amount}")
        return

    def get_transactions(self) -> list[str]:
        return self.transactions.copy()
    
    def __repr__(self) -> str:
        return (
            f"BankAccount(owner={self.owner!r}, "
            f"balance={self.balance:.2f})"
        )


# Test your class
account = BankAccount("Ali", 5000)

account.deposit(2000)
account.withdraw(1500)

print(account)
print("Balance:", account.balance)

try:
    account.deposit(-500)
except ValueError as e:
    print("Error:", e)


try:
    account.withdraw(10000)
except InsufficientFundsError as e:
    print("Error:", e)


try:
    account.withdraw(0)
except ValueError as e:
    print("Error:", e)
    
for transaction in account.get_transactions():
    print(transaction)
