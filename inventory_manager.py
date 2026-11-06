import os
import json


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

    def set_price(self, new_price):
        if new_price <= 0:
            return False
        else:
            self.price = new_price
            return True

    def to_dict(self):
        return {"name": self.name, "price": self.price, "quantity": self.quantity}


def ask_float(prompt):
    while True:
        try:
            number = float(input(prompt))
        except ValueError:
            print("Please enter a number, e.g. 12.50")
            continue

        if number > 0:
            return number
        print("Must be more than 0.")


def ask_int(prompt, minimum):
    while True:
        try:
            number = int(input(prompt))
        except ValueError:
            print("Please enter a whole number, e.g. 10")
            continue

        if number >= minimum:
            return number
        print(f"Must be at least {minimum}.")


def list_products(products):
    if not products:
        print("No products yet.")
        return

    for number, product in enumerate(products, start=1):
        print(f"{number}. {product.name}: R{product.price:.2f} - {product.quantity} in stock")


def add_product(products):
    while True:
        name = input("Product name: ").strip()
        if not name:
            print("Name can't be empty.")
        else:
            break

    price = ask_float("Price: ")
    quantity = ask_int("Quantity: ", 0)

    new_product = Product(name, price, quantity)
    products.append(new_product)
    print(f"✅ Added {new_product.name}: R{new_product.price:.2f} - {new_product.quantity} in stock")


def choose_product(products):
    while True:
        try:
            product_number = int(input("Please choose product number: "))
        except ValueError:
            print("Please enter a number.")
            continue

        if 1 <= product_number <= len(products):
            return product_number - 1
        else:
            print("No product with that number")


def update_stock(products):
    if not products:
        print("No products yet.")
        return

    list_products(products)
    index = choose_product(products)
    product = products[index]

    print(f"{product.name}: R{product.price:.2f} - {product.quantity} in stock")
    print("1. Add stock")
    print("2. Remove stock")
    print("3. Change price")
    print("4. Remove product")
    print("5. Back")
    choice = input("Choose an option: ")

    if choice == "1":
        amount = ask_int("Amount to add: ", 1)
        product.add_stock(amount)
        print(f"✅ {product.name} now has {product.quantity} in stock")

    elif choice == "2":
        amount = ask_int("Amount to remove: ", 1)
        if product.remove_stock(amount):
            print(f"✅ {product.name} now has {product.quantity} in stock")
        else:
            print(f"❌ Not enough stock (only {product.quantity})")

    elif choice == "3":
        new_price = ask_float("New price: ")
        if product.set_price(new_price):
            print(f"✅ {product.name} now costs R{product.price:.2f}")
        else:
            print("❌ Price must be more than 0")

    elif choice == "4":
        sure = input(f"Remove {product.name}? (y/n): ").strip().lower()
        if sure == "y":
            removed = products.pop(index)
            print(f"🗑️ Removed {removed.name}")
        else:
            print("Nothing removed.")

    elif choice == "5":
        return

    else:
        print("Invalid option.")


def save_products(products):
    saved_products = []
    for product in products:
        saved_products.append(product.to_dict())

    with open("inventory.json", "w") as file:
        json.dump(saved_products, file, indent=2)


def load_products():
    if not os.path.exists("inventory.json"):
        return []

    with open("inventory.json", "r") as file:
        data = json.load(file)

    products = []
    for item in data:
        products.append(Product(item["name"], item["price"], item["quantity"]))
    return products


products = load_products()

while True:
    print()
    print("=== Inventory Manager ===")
    print("1. List products")
    print("2. Add a product")
    print("3. Update product")
    print("4. Quit")
    choice = input("Choose an option: ")

    if choice == "1":
        list_products(products)
    elif choice == "2":
        add_product(products)
        save_products(products)
    elif choice == "3":
        update_stock(products)
        save_products(products)
    elif choice == "4":
        print("Goodbye!")
        break
    else:
        print("Invalid option, please try again.")