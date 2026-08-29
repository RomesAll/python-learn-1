#Подход 1: Прямой доступ (PriceCalculator.product.get_name())

class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def get_name(self):
        return self.name

    def get_price(self):
        return self.price

class PriceCalc:
    def __init__(self, product, disc=0.0, tax=0.0):
        self.product = product
        self.disc = disc
        self.tax = tax

    def calc(self):
        result = self.product.price
        result *= (1 - self.disc)
        result *= (1 + self.tax)
        return result

milk = Product('Milk', 1000)
calc = PriceCalc(milk, disc=0.6, tax=0.1)

print(calc.product.get_name())
print(calc.product.get_price())
print(calc.calc())
