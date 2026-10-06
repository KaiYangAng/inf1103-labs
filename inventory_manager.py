import json

def show_menu():
    print("----------- MENU -----------")
    print("1. Display All Products")
    print("2. Add Product")
    print("3. Update Stock")
    print("4. Search Product")
    print("5. Save Inventory")
    print("6. Exit")
    print("----------------------------")

#Option 1
def display_all(inventory): 
    print("Current Inventory")
    print("----------------------------")
    for item in inventory:
        print(f"ID: {item['ID']} | Name: {item['Name']} | Price: ${item['Price']:.2f} | Stock: {item['Stock']}")
    print("----------------------------")

#Option 2
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

def add_product(inventory):
    new_id = input("Enter Product ID: ")
    new_name = input("Enter Product Name: ")
    new_price = get_valid_float("Enter Product Price: ")
    new_stock = get_valid_int("Enter Product Stock: ")
    
    new_product = {"ID": new_id, "Name": new_name, "Price": new_price, "Stock": new_stock}
    inventory.append(new_product)
    print("Product added successfully.")

#Option 3
def update_stock(inventory):
    product_id = input("Enter Product ID to update stock: ")
    for item in inventory:
        if item["ID"] == product_id:
            print ("Product found:", item["Name"])
            print ("Current Stock:", item["Stock"])
            new_stock = get_valid_int("\nEnter new stock quantity: ")
            item["Stock"] = new_stock
            print("\nStock updated successfully!")
            return
    print("Product not found.")

#Option 4
def search_product(inventory):
    product_id = input("Enter Product ID to search: ")
    for item in inventory:
        if item["ID"] == product_id:
            print("Product Found")
            print("----------------------------")
            print(f"ID: {item['ID']}")
            print(f"Name: {item['Name']}")
            print(f"Price: ${item['Price']:.2f}")
            print(f"Stock: {item['Stock']}")
            print("----------------------------")
            return
    print("Product not found.")

#Main Program
print("========================================")
print("INVENTORY MANAGEMENT SYSTEM")
print("========================================")

# Load existing inventory from JSON file
product = [
        {"ID": "P001", "Name": "Laptop", "Price": 1200.00, "Stock": 15},
        {"ID": "P002", "Name": "Mouse", "Price": 25.50, "Stock": 40},
        {"ID": "P003", "Name": "Keyboard", "Price": 45.00, "Stock": 25}
    ]

while True:
    show_menu()
    user_option = input("Enter option: ")

    if user_option == "1":
        display_all(product)
    elif user_option == "2":
        add_product(product)
    elif user_option == "3":
        update_stock(product)
    elif user_option == "4":
        search_product(product)
    elif user_option == "6":
        print("Thank you for using Inventory Management System.")
        print("Program terminated.")
        break
