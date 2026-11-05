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


def add_product(products):
    name = input("Product name: ")

    while True:
        try:
            price = float(input("Price: "))
            break
        except ValueError:
            print("Price must be a number, e.g. 22.99")

    while True:
        try:
            quantity = int(input("Quantity: "))
            break
        except ValueError:
            print("Quantity must be a whole number, e.g. 10")

    new_product = Product(name, price, quantity)
    products.append(new_product)
    print(f"✅ Added {new_product.name}: R{new_product.price:.2f} - {new_product.quantity} in stock")
        
products = [
    Product("Coffee", 45.0, 20),
    Product("Tea", 30.50, 12),
]

while True:
    print()
    print("=== Inventory Manager ===")
    print("1. List products")
    print("2. Add a product")
    print("3. Quit")
    choice = input("Choose an option: ")

    if choice == "1":
        list_products(products)
    elif choice == "2":
        add_product(products)
        
    elif choice == "3":
        print("Goodbye!")
        break

    else:
        print("Invalid option, please try again.")