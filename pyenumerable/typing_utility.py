from collections.abc import Callable
from typing import Protocol

type Comparer[T] = Callable[[T,T], bool]


class Comparable(Protocol):
    def __eq__[T](self: T, other: T, /) -> bool: ...

    def __lt__[T](self: T, other: T, /) -> bool: ...

    def __gt__[T](self: T, other: T, /) -> bool: ...

    def __le__[T](self: T, other: T, /) -> bool: ...

    def __ge__[T](self: T, other: T, /) -> bool: ...


class Addable(Protocol):
    def __add__[T](self: T, x: T, /) -> T: ...
