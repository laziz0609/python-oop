class Product:
    def __init__(self, name: str, price: float, category: str, in_stock: bool):
        self.name = name
        self.price = price
        self.category = category
        self.in_stock = in_stock
        
        
    def check_stock(self):
        if self.in_stock:
            print(f"{self.name} omborda mavjud ✅")
            
        else:
            print(f"{self.name} hozirda tugagan ❌")
            
            
            
p1 = Product("olma", 12000, "meva", True)
p2 = Product("apelsin", 32000, "meva", True)
p3 = Product("anor", 22000, "meva", False)
p4 = Product("guruch", 12000, "dukkakli", True)
p5 = Product("choynak", 122000, "chinni", False)

products = [p1, p2, p3, p4, p5]

total = sum(map(lambda x: x.price, filter(lambda x: x.in_stock, products)))
print(f"Ombordagi mahsulotlar narxi: {total}")