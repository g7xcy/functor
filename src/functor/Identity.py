from typing import Callable, TypeVar

from .Functor import Functor

T = TypeVar("T")
U = TypeVar("U")


class Identity(Functor[T]):
    def __init__(self, value: T):
        self.value = value

    @classmethod
    def of(cls, value: T) -> "Identity[T]":
        return Identity(value)

    def fmap(self, f: Callable[[T], U]) -> "Identity[U]":
        return Identity.of(f(self.value))
