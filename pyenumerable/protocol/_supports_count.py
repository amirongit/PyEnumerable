from collections.abc import Callable
from typing import Protocol, overload


class SupportsCount[TSource](Protocol):
    @overload
    def count_(self, /) -> int: ...

    @overload
    def count_(self, predicate: Callable[[TSource], bool], /) -> int: ...
