from typing import Protocol, runtime_checkable


@runtime_checkable
class Speakable(Protocol):
    def speak(self) -> str:
        pass


class Dog:
    def speak(self) -> str:
        return 'gav'

d = Dog()
print(d.speak(), isinstance(d, Speakable))