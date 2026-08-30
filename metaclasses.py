from typing import Callable
from uuid import UUID, uuid4


def logger(func: Callable):
    def wrapper(*args, **kwargs):
        print(f'Вызывается метод \"{func.__name__}\", с аргументами {args[1:] if args[1:] else ''}, {kwargs}')
        res = func(*args, **kwargs)
        print(f'Результат вызова метода \"{func.__name__}\": {res}')
        return res
    return wrapper


class WrapLoggingMeta(type):
    def __new__(cls, name, bases, attrs):
        for attr, value in attrs.items():
            if callable(value):
                attrs[attr] = logger(value)
        return super().__new__(cls, name, bases, attrs)


class OrderRepository(metaclass=WrapLoggingMeta):
    def get_order(self, order_id: UUID):
        return 'order'

o = OrderRepository()
o.get_order(order_id=uuid4())