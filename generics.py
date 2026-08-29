from typing import Type, Generic, TypeVar

T = TypeVar('T')

def get_first(items: list[T]) -> T | None:
    return items[0] if items else None

first_int = get_first([1, 2, 3])
first_str = get_first(["a", "b"])
first_float = get_first([1.0, 2.0])
