class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity


product1 = Product("Coffee", 45.0, 20)
product2 = Product("Tea", 30.50, 12)

print(f"{product1.name}: R{product1.price}, {product1.quantity} in stock")
print(f"{product2.name}: R{product2.price}, {product2.quantity} in stock")