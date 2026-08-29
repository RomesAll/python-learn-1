from typing import Type, Generic, TypeVar

T = TypeVar('T')

def get_first(items: list[T]) -> T | None:
    return items[0] if items else None

first_int = get_first([1, 2, 3])
first_str = get_first(["a", "b"])
first_float = get_first([1.0, 2.0])


class Box(Generic[T]):
    def __init__(self, data: T):
        self.data = data

    def get(self) -> T:
        return self.data

    def set(self, data: T) -> None:
        self.data = data

b = Box[int](data=12)
res = b.get()
print(res)

from typing import TypeVar, Generic, List, Optional
from abc import ABC, abstractmethod

T = TypeVar('T')


class Repository(Generic[T], ABC):
    @abstractmethod
    def save(self, entity: T) -> None:
        pass

    @abstractmethod
    def get(self, id: int) -> Optional[T]:
        pass

    @abstractmethod
    def get_all(self) -> List[T]:
        pass


class User:
    def __init__(self, id: int, name: str):
        self.id = id
        self.name = name


class UserRepository(Repository[User]):
    def __init__(self):
        self._users: dict[int, User] = {}

    def save(self, entity: User) -> None:
        self._users[entity.id] = entity

    def get(self, id: int) -> Optional[User]:
        return self._users.get(id)

    def get_all(self) -> List[User]:
        return list(self._users.values())


# Использование
repo = UserRepository()
user = User(1, "Alice")
repo.save(user)
retrieved = repo.get(1)
print(retrieved.name)  # "Alice"