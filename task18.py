class Product:
    def __init__(self, name: str, price: float, category: str):
        self.name = name
        self.price = price
        self.category = category
        
        
    def info(self):
        print(f"{self.name} - {self.price}")
            
            
            
p1 = Product("olma", 12000, "meva")
p2 = Product("apelsin", 32000, "meva")
p3 = Product("anor", 22000, "meva")
p4 = Product("guruch", 12000, "dukkakli")
p5 = Product("choynak", 122000, "chinni")
p6 = Product("piyola", 2000, "chinni")

products = [p1, p2, p3, p4, p5, p6]

max_product = max(products, key=lambda x: x.price)
max_product.info()