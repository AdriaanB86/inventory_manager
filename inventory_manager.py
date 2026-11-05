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


def list_products(products):
    for number, product in enumerate(products, start=1):
        print(f"{number}. {product.name}: R{product.price:.2f} - {product.quantity} in stock")


products = [
    Product("Coffee", 45.0, 20),
    Product("Tea", 30.50, 12),
]

while True:
    print()
    print("=== Inventory Manager ===")
    print("1. List products")
    print("2. Quit")
    choice = input("Choose an option: ")

    if choice == "1":
        list_products(products)
    elif choice == "2":
        print("Goodbye!")
        break
    else:
        print("Invalid option, please try again.")