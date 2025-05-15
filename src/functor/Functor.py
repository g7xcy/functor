from abc import ABC, abstractmethod
from typing import Callable, Generic, TypeVar

T = TypeVar("T")
U = TypeVar("U")


class Functor(ABC, Generic[T]):
    val: T

    @classmethod
    @abstractmethod
    def of(cls, val: T) -> "Functor[T]":
        pass

    @abstractmethod
    def fmap(self, f: Callable[[T], U]) -> "Functor[U]":
        pass
