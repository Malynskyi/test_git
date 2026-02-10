class Product:
    def __init__(self, name, category, price, quantity):
        self.name = name
        self.category = category
        self.price = price
        self.quantity = quantity

    def change_price(self, new_price):
        self.price = new_price

    def change_quantity(self, new_quantity):
        self.quantity = new_quantity



class Customer:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.orders = []

    def add_order(self, order):
        self.orders.append(order)



class Order:
    def __init__(self):
        self.products = []
        self.total_sum = 0

    def add_product(self, product):
        self.products.append(product)
        self.calculate_total()

    def calculate_total(self):
        self.total_sum = 0
        for product in self.products:
            self.total_sum += product.price



def load_products_from_txt(filename):
    products = []

    file = open(filename, "r", encoding="utf-8")
    for line in file:
        data = line.strip().split(",")

        name = data[0]
        category = data[1]
        price = float(data[2])
        quantity = int(data[3])

        product = Product(name, category, price, quantity)
        products.append(product)

    file.close()
    return products



products = load_products_from_txt("products.txt")

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