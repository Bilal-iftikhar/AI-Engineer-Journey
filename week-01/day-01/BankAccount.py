class BankAccount:
    def __init__(self, account_holder:str, balance:float):
        self.balance = balance
        self._account_holder = account_holder

    @property
    def balance(self)->float:
      return self._balance
    @balance.setter
    def balance(self, value):
      if(value <= 0):
        raise ValueError('Value should be the positive value')
      self._balance = value
    

    def deposit(self,amount)->None:
        if(amount <= 0 ):
            raise ValueError("Amount should be in positive value")
        self.balance += amount  
        return

    def withdraw(self, amount)->None:
        if(amount < 0 ):
            raise ValueError("Amount should be in positive value")
        if amount > self.balance:
            raise ValueError("Insufficient funds")
        
        self.balance -= amount  
        return

    def __repr__(self)->str:
        return (
                f"BankAccount(owner={self._account_holder!r}, "
                f"balance={self.balance:.2f})"
            )

account = BankAccount("Bilal", 5000)

account.deposit(2000)
account.withdraw(1500)

print(account.balance)
print(account)