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