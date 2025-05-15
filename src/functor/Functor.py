from abc import ABC, abstractmethod
from typing import Callable, Generic, TypeVar

T = TypeVar("T")
U = TypeVar("U")


class Functor(ABC, Generic[T]):
    value: T

    @classmethod
    @abstractmethod
    def of(cls, val: T) -> "Functor[T]":
        raise NotImplementedError("Cannot instantiate Functor directly.")

    @abstractmethod
    def fmap(self, f: Callable[[T], U]) -> "Functor[U]":
        pass
