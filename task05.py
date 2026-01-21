class Product:
    def __init__(self, name: str, price: float, category: str, in_stock: bool):
        self.name = name
        self.price = price
        self.category = category
        self.in_stock = in_stock
        
    
    
p1 = Product("olma", 15, "meva", True)
p2 = Product("mandarin", 35, "meva", False)
p3 = Product("guruch", 15, "dukkakli mahsulotlar", True)

products = [p1, p2, p3]

for product in products:
    print(f"{product.name} - {product.price}")