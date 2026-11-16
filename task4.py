class Account:
    def __init__(self, owner,balance):
        self.owner =owner
        self.balance = balance

    def withdraw(self, amount):
        if amount > self.balance:
            raise ValueError(
                f"Insufficient fund: balance {self.balance},requested {amount}"
            )
        self.balance -= amount


class savingsAccount(Account):
    def __init__(self, owner, balance):
        super().__init__(owner, balance)
        self.min_balance = 500

    def withdraw(self, amount):
        if self.balance - amount < self.min_balance:
            raise ValueError(
                f"Insufficient funds: balance {self.balance}, requested {amount}"
            )
        self.balance -= amount


vijay = savingsAccount("Vijay",1500)

try:
    vijay.withdraw(1200)
except ValueError as e:
    print("Error:", e)


try:
    vijay.withdraw(800)
    print(f"Vijay withdraw 800 -> balance {vijay.balance}")
except ValueError as e:
    print("Error:", e)

print(isinstance(vijay, Account))




