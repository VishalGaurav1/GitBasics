class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def display_info(self):
        return f"Product Name: {self.name}, Price: ${self.price:.2f}"

if __name__ == "__main__":
    product1 = Product("Laptop", 999.99)
    print(product1.display_info())