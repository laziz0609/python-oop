class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance
    
    def deposit(self, amount):
        if amount > 0 :
            self.balance += amount
            print(f"{self.balance}, {amount} qo'shildi")
    
    def withdraw(self, amount):
        if amount < self.balance:
            self.balance -= amount
            print(f"{self.balance}, {amount} ayrildi")