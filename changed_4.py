class ProductFactory:
    @staticmethod
    def create_product(name, category, price, quantity):
        return Product(name, category, price, quantity)
    

class ProductStorage:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(ProductStorage, cls).__new__(cls)
            cls._instance.products = []
        return cls._instance

    def load_from_txt(self, filename):
        with open(filename, "r", encoding="utf-8") as file:
            for line in file:
                data = line.strip().split(",")

                product = ProductFactory.create_product(
                    name=data[0],
                    category=data[1],
                    price=float(data[2]),
                    quantity=int(data[3])
                )
                self.products.append(product)

    def get_products(self):
        return self.products
    

# Singleton
storage = ProductStorage()
storage.load_from_txt("products.txt")

products = storage.get_products()

customer = Customer("Dmytro", "dimamalinskij671@gmail.com")

order = Order()
order.add_product(products[0])
order.add_product(products[1])

customer.add_order(order)

print("Customer:", customer.name)
print("Email:", customer.email)
print("Order total:", order.total_sum)

print("\nProducts in stock:")
for p in products:
    print(p.name, "-", p.quantity)