class Book:
    def __init__(self, title: str, author: str, is_read: bool):
        self.title = title
        self.author = author
        self.is_read = is_read
        
    
    def mark_as_read(self):
        self.is_read = True
        print(f"{self.title} o‘qilgan deb belgilandi")
        
        
    def status(self):
        if self.is_read:
            print("O‘qilgan")
        
        else:
            print("O‘qilmagan")
            

book1 = Book("dunyomimig ishlari", "o'tkir hoshimov", True)
book2 = Book("men", "fotih duman", True)
book3 = Book("iymon", "shayx muhammad sodiq muhammad yusuf", False)
book4 = Book("oq kema", "chingiz aytmatov", False)


books = [book4, book1, book2, book3]
book4.mark_as_read()

for book in books:
    print(f"{book.title} - {book.is_read}")
