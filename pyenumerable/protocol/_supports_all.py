from collections.abc import Callable
from typing import Protocol, overload


class SupportsAll[TSource](Protocol):
    @overload
    def all(self, /) -> bool: ...

    @overload
    def all(self, predicate: Callable[[TSource], bool], /) -> bool: ...
