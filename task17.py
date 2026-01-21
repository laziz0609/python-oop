class BankAccount:
    
    def __init__(self, owner: str, balamce: float):
        self.owner = owner
        self.balance = balamce
        
    def deposit(self, amount: float):
        if amount > 0:
            self.balance += amount
        
        else:
            print("amount musbat bo'lishligi kerak")
            
    
    def withdraw(self, amount: float):
        if amount < self.balance and amount > 0:
            self.balance -= amount

        else:
            print("xatolik")
            
            
    def show_balance(self):
        print(self.balance)
        

ow1 = BankAccount("ali", 1500)
ow2 = BankAccount("vali", 2500)
ow3 = BankAccount("g'ani", 3500)
ow4 = BankAccount("soli", 5500)
ow5 = BankAccount("sami", 35600)

result = [ow1, ow2, ow3, ow4, ow5]

total = 0
for ow in result:
    total += ow.balance
    
print(total)