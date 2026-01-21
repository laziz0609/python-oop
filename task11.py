class Book:
    def __init__(self, title: str, author: str, is_read: bool):
        self.title = title
        self.author = author
        self.is_read = is_read
        
    
    def mark_as_read(self):
        self.is_read = True
        print("Kitob o‘qilgan deb belgilandi")
        
        
    def status(self):
        if self.is_read:
            print("O‘qilgan")
        
        else:
            print("O‘qilmagan")