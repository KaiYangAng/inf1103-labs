class Product:
    def __init__(self, id, name, price, quantity):
        self.id = str(id)
        self.name = str(name)
        self.__price = float(price)
        self.__quantity = int(quantity)

    def __str__(self):
        return f"Product(id={self.id}, name={self.name}, price={self.__price}, quantity={self.__quantity})"

class Inventory:
    def __init__(self):
        self.products = []

    def add_product(self, product):
        self.products.append(product)

    def update_stock(self, product_id, new_quantity):
        for product in self.products:
            if product.id == str(product_id):
                product.__quantity = int(new_quantity)
                return True
        return False

    def search_product(self, product_id):
        for product in self.products:
            if product.id == str(product_id):
                return product
        return None

    def display_inventory(self):
        print("Current Inventory")
        print("----------------------------")
        for product in self.products:
            print(f"ID: {product.id} | Name: {product.name} | Price: ${product.__price:.2f} | Stock: {product.__quantity}")
        print("----------------------------")

inv = Inventory()
inv.add_product(Product("P001", "Laptop", 1200, 15))
inv.update_stock("P001", 50)
print(inv.search_product("P001"))   # what's the stock now?
inv.display_inventory()             # what happens here?