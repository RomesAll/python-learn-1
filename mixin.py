
class Product:
    def __init__(self, name, price):
        self.name = name
        self._price = price

    def price(self):
        return self._price


class Discount:
    def price(self):
        return super().price() * 0.4


class Taxes:
    def price(self):
        return super().price() * 0.1


class Order(Discount, Taxes, Product):
    pass


o = Order('milk', 1000).price()
print(o)