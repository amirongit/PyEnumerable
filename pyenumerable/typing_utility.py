from collections.abc import Callable
from typing import Protocol, runtime_checkable

type Comparer[T] = Callable[[T,T], bool]


@runtime_checkable
class Comparable(Protocol):
    def __eq__(self, other: object, /) -> bool: ...

    def __lt__(self, other: object, /) -> bool: ...

    def __gt__(self, other: object, /) -> bool: ...

    def __le__(self, other: object, /) -> bool: ...

    def __ge__(self, other: object, /) -> bool: ...
