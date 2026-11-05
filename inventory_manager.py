class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    def total_value(self):
        return self.price * self.quantity

    def add_stock(self, amount):
        self.quantity = self.quantity + amount

    def remove_stock(self, amount):
        if amount > self.quantity:
            return False
        self.quantity = self.quantity - amount
        return True

product1 = Product("Coffee", 45.0, 20)
product2 = Product("Tea", 30.50, 12)
product1.add_stock(10)

if product2.remove_stock(5):
    print("Sold 5 tea")
else:
    print("Not enough tea in stock")

print(f"Coffee stock value: R{product1.total_value():.2f}")
print(f"{product1.name}: R{product1.price:.2f}, {product1.quantity} in stock")
print(f"{product2.name}: R{product2.price:.2f}, {product2.quantity} in stock")
