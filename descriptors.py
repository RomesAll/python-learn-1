

class PositiveNumber:
    def __set_name__(self, owner, name):
        self.name = name

    def __get__(self, obj, obj_type):
        return obj.__dict__.get(self.name)

    def __set__(self, obj, value):
        obj.__dict__[self.name] = value

class Order:
    amount = PositiveNumber()


order = Order()
order.amount = 100
print(order.__dict__)
print(order.amount)

# order.__dict__ = {
#     'amount': 100  # теперь здесь число!
# }
# так а почему при обращении к order.amount вызывается дескриптор а не число?
# дело в том что дескрипторы имеют приоритет над обычными атрибутами!!!!