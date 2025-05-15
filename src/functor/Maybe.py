from typing import Callable, TypeVar, Optional, Union

from .Functor import Functor

T = TypeVar("T")
U = TypeVar("U")


class Maybe(Functor[T]):
    def __init__(self, value: Optional[T]) -> Union["Just[T]", "Nothing"]:
        self.value = value

    @classmethod
    def of(cls, value: Optional[T]) -> Union["Just[T]", "Nothing"]:
        if value is None:
            return Nothing()
        return Just.of(value)

    def fmap(self, f: Callable[[T], U]) -> "Maybe[U]":
        pass


class Just(Maybe[T]):
    def __init__(self, value: T):
        super().__init__(value)

    @classmethod
    def of(cls, value: T) -> "Just[T]":
        return Just(value)

    def fmap(self, f: Callable[[T], U]) -> "Maybe[U]":
        t = f(self.value)
        if t is None:
            return Nothing()
        return Just(t)


class Nothing(Maybe[None]):
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self):
        super().__init__(None)

    @classmethod
    def of(cls) -> "Nothing":
        return cls._instance or cls()

    def fmap(self, _: Callable[[T], U]):
        return self
