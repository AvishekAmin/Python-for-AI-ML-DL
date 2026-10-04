class Product:
    count = 0

    def __init__(self, name, price):
        self.name = name
        self.price = price
        Product.count += 1

    def get_info(self):     # instance method
        print(f"Price of {self.name} is: {self.price}")

    @classmethod
    def get_count(cls):    # class method
        print(f"Total products in store: {cls.count}")

    @staticmethod
    def calc_discount(price, discount):     # static method
        print(f"Discounted price: {price - (price * discount / 100)}")

p1 = Product("Smartphone", 40_000)
p2 = Product("Laptop", 70_000)
p3 = Product("Pen", 10)

p1.get_info()
Product.get_count()
p1.calc_discount(p1.price, 10)