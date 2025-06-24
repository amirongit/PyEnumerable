from collections.abc import Callable
from typing import Protocol, overload


class SupportsAll[TSource](Protocol):
    @overload
    def all_(self, /) -> bool: ...

    @overload
    def all_(self, predicate: Callable[[TSource], bool], /) -> bool: ...
