class User:
    def __init__(self, username: str, email: str, is_active: bool):
        self.username = username
        self.email = email
        self.is_active = is_active
        
    def activate(self):
        self.is_active = True
        print("Faollashdi")
    
    def deactivate(self):
        self.is_active = False
        print("to'xtadi")
    
    def info(self):
        print(f"{self.username}, {self.email}, {self.is_active}")  

p1 = User("asd", "asd@gamil.com", True)

p1.deactivate()
p1.info()