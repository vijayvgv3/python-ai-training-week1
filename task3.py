class InsufficientFundsError(Exception):
   pass

class Account:
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
          self.balance += amount
          print (f"{self.owner} deposited {amount} -> balance {self.balance}")

    def withdraw(self, amount):
            if amount > self.balance:
                raise InsufficientFundsError(f"Insuuficient funds: balance {self.balance}, requested {amount}")
            
            self.balance -= amount
            print(f"{self.owner} withdraw {amount} -> balance {self.balance}")

    def show(self):
         print(f"Account Owner: {self.owner}")
         print(f"Current Balance: {self.balance}")

# Create Account
account = Account ("vijay",  1000)

# Deposit and withdraw
try:
     account.deposit(500)
     account.withdraw(2000)

except InsufficientFundsError as e:
     print("Error:", e)

finally:
     print("Transaction finished")

  

