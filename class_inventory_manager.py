import json

class Product:
    def __init__(self, product_id, name, price, stock): 
        self.__product_id = str(product_id)
        self.__name = str(name)
        self.__price = float(price)
        self.__stock = int(stock)

    def get_product_id(self): 
        return self.__product_id
    
    def update_stock(self, quantity):
        if quantity < 0:
                print("Stock cannot be negative.")
                return False
        else:
                self.__stock = quantity
                return True

    def display_information(self):
        print(f"ID: {self.__product_id} | Name: {self.__name} | Price: ${self.__price:.2f} | Stock: {self.__stock}")

    def to_dict(self):
        return {
            "ID": self.__product_id,
            "Name": self.__name,
            "Price": self.__price,
            "Stock": self.__stock
        }

class Inventory:
    def __init__(self):
        self.__products = []

    def add_product(self, product):
        self.__products.append(product)

    def search_product(self, product_id):
        for product in self.__products:
            if product.get_product_id() == product_id:
                return product
        return None

    def update_stock(self, product_id, quantity):
        product = self.search_product(product_id)
        if product is None:
            return False
        else:
             return product.update_stock(quantity)

    def display_all(self):
        for product in self.__products:
            product.display_information()

    def get_all_products(self):
        return self.__products

#Main Program
def get_valid_float(prompt):
    while True:
        try:
            value = float(input(prompt))
            return value
        except ValueError:
            print("Error: Please enter a valid number.")

def get_valid_int(prompt):
    while True:
        try:
            value = int(input(prompt))
            return value
        except ValueError:
            print("Error: Please enter a whole number.")

def show_menu():
    print("----------- MENU -----------")
    print("1. Display All Products")
    print("2. Add Product")
    print("3. Update Stock")
    print("4. Search Product")
    print("5. Save Inventory")
    print("6. Exit")
    print("----------------------------")

def handle_add_product(inventory):
    print("Add New Product")
    new_id = input("Enter Product ID: ")
    new_name = input("Enter Product Name: ")
    new_price = get_valid_float("Enter Product Price: ")
    new_stock = get_valid_int("Enter Product Stock: ")

    new_product = Product(new_id, new_name, new_price, new_stock)
    inventory.add_product(new_product)
    print("Product added successfully.")

def handle_update_stock(inventory):
    product_id = input("Enter Product ID to update stock: ")
    product = inventory.search_product(product_id)

    if product is None:
        print("Product not found.")
        return
    print ("Product found:", product.get_product_id())

    new_stock = get_valid_int("\nEnter new stock quantity: ")

    if product.update_stock(new_stock):
        print("\nStock updated successfully!")
    else:
        print("\nFailed to update stock.")

def handle_search(inventory):
    product_id = input("Enter Product ID to search: ")
    product = inventory.search_product(product_id)
    if product:
        print("Product found:")
        product.display_information()
    else:
        print("Product not found.")

def save_inventory(inventory, filename="inventory.json"):
    data = []
    for product in inventory.get_all_products():
        data.append(product.to_dict())

    with open(filename, "w") as file:
        json.dump(data, file, indent=4)

def load_inventory(filename="inventory.json"):
    inventory = Inventory()                        

    try:
        with open(filename, 'r') as file:
            data = json.load(file)               # data is a LIST of dicts

        for d in data:
            product = Product(d["ID"], d["Name"], d["Price"], d["Stock"])
            inventory.add_product(product)

        print("inventory.json found.")
        print("Inventory loaded successfully.")

    except FileNotFoundError:
        print("Inventory file not found. Starting with an empty inventory.")

    return inventory

def main():
    print("========================================")
    print("INVENTORY MANAGEMENT SYSTEM")
    print("========================================")

    inventory = load_inventory()

    while True:
        show_menu()
        user_option = input("Enter option: ")

        if user_option == "1":
            inventory.display_all()
        elif user_option == "2":
            handle_add_product(inventory)
        elif user_option == "3":
            handle_update_stock(inventory)
        elif user_option == "4":
            handle_search(inventory)
        elif user_option == "5":
            print("Saving inventory...")
            save_inventory(inventory)
            print("Inventory saved successfully to inventory.json.")
        elif user_option == "6":
            print("Saving inventory before exit...")
            save_inventory(inventory)
            print("Inventory saved successfully.")
            print("Thank you for using Inventory Management System.")
            print("Program terminated.")
            break
        else:
            print("Invalid option. Please try again.")

main()